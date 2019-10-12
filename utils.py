# -*- coding: utf-8 -*-
import re


class Filter():

    reg = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - -\s+' \
          r'\[(?P<datetime>\S+\s\S+)\]\s+' \
          r'"(?P<method>\w+)\s+' \
          r'(?P<uri>\B/[-A-Za-z0-9+&@#/%?=~_|!:,.;]*)\s+' \
          r'(?P<protocol>HTTP\S+)"\s+' \
          r'(?P<code>\d+)\s' \
          r'(?P<content_length>\d+)'

    def _filter_log(self, file_path, mode='r+'):
        """
            过滤日志信息,
        :param file_path: 日志文件路径
        :param mode: 文件打开方式，默认'r+'
        :return:返回过滤异常日志之后的日志列表
        """

        # 分析文件，按行读取
        # TODO: 异常处理未做
        log_list = []
        with open(file_path, mode) as log_fp:
            while True:
                log_buf = log_fp.readline()
                if not log_buf:
                    break
                res = re.match(self.reg, log_buf)
                if res:
                    log_list.append(res.groupdict())
        return log_list

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
        for uri_type in type_list:
            for log in filter_logs:
                if uri_type in log.get('uri', None):
                    continue
                log_list.append(log)
        return log_list
