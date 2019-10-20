# -*- coding: utf-8 -*-
import re


def read_log_file(file_path):
    """
        读取日志文件
    :param file_path: 日志文件路径
    :return: 返回日志文件列表
    """

    log_list = []
    mode = 'r+'
    with open(file_path, mode) as log_fp:
        while True:
            log_buf = log_fp.readline()
            if not log_buf:
                break
            log_list.append(log_buf)
    return log_list


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
        log_list = read_log_file(file_path)
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
        filter_logs = self._parser_log(file_path)
        filter_types = ['css', 'js'] if file_types is None else file_types
        for log in filter_logs:
            for filter_type in filter_types:
                url = log.get('url')
                if url.endswith(filter_type):
                    break
            if not url.endswith(filter_type):
                log_list.append(log)

        return log_list
