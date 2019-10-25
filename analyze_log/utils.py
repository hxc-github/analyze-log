# -*- coding: utf-8 -*-
import re
import functools

LOG_PARSERS = []


def parse_log_file(file_path):
    """
        解析日志文件
    :param file_path: 日志文件路径
    :type file_path: string
    :return:日志信息生成器
    """

    with open(file_path, 'r') as log_fp:
        for log in log_fp:
            yield _parse_log(log)


def _parse_log(text):

    for parser in LOG_PARSERS:
        res = parser(text)
        if res:
            return res


def _parser_log_by_ipv4(text):

    reg = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - -\s+' \
          r'\[(?P<datetime>\S+\s\S+)\]\s+' \
          r'"(?P<method>\w+)\s+' \
          r'(?P<url>\B/[-A-Za-z0-9+&@#/%?=~_|!:,.;]*)\s+' \
          r'(?P<protocol>HTTP\S+)"\s+' \
          r'(?P<code>\d+)\s' \
          r'(?P<content_length>\d+)'
    res = re.match(reg, text)
    if res:
        return res.groupdict()


LOG_PARSERS.append(_parser_log_by_ipv4)


def _filter_func_by_type(log, filter_types):
    """
        根据filter_types，滤除日志类型
    :param log:
    :param filter_types:
    :return:
    """
    if not log:
        return False
    log_type = log['url'].split('.')[-1]

    # 滤除不需要的日志
    if log_type in filter_types:
        return False
    else:
        return True


def log_filter(logs, filter_types=None):
    """
        根据filter_types，滤除日志类型
    :param logs: 日志迭代器
    :type logs: 迭代器
    :param filter_types: 需要滤除的日志类型，默认滤除css和js格式
    :type filter_types: list
    :return: 滤除后的日志列表
    """
    filter_types = ['css', 'js'] if filter_types is None else filter_types
    func = functools.partial(_filter_func_by_type, filter_types=filter_types)
    logs = filter(func, logs)
    return logs
