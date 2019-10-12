# -*- coding: utf-8 -*-
import utils
import re


class Parser(object):

    def __init__(self):
        self.reg = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - -\s+' \
                   r'\[(?P<datetime>\S+\s\S+)\]\s+' \
                   r'"(?P<method>\w+)\s+' \
                   r'(?P<url>\B/[-A-Za-z0-9+&@#/%?=~_|!:,.;]*)\s+' \
                   r'(?P<protocol>HTTP\S+)"\s+' \
                   r'(?P<code>\d+)\s' \
                   r'(?P<content_length>\d+)'

    def _parser_log(self, file_path):
        """
            解析日志信息,
        :param file_path: 日志文件路径
        :return:返回日志解析之后的日志
        """

        filter_logs = list()
        log_list = utils.read_log_file(file_path)
        for log in log_list:
            res = re.match(self.reg, log)
            if res:
                filter_logs.append(res.groupdict())
        return filter_logs

    def filter_log_by_type(self, file_path, file_types=None):
        """
            按照过滤的类型滤除不需要的日志
        :param file_path: 日志文件路径
        :param file_types: URL需要过滤的文件类型
        :return: 返回按照类型过滤日志之后的日志列表
        """

        log_list = []
        filter_logs = self._filter_log(file_path)
        type_list = ['css', 'js'] if file_types is None else file_types
        for url_type in type_list:
            for log in filter_logs:
                if url_type in log.get('url', None):
                    continue
                log_list.append(log)
        return log_list
