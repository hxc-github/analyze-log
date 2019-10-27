# -*- coding: utf-8 -*-
import re


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


# 支持的访问IP类型，目前只支持IPv4
IP_TYPE = {
    'IPv4': _parser_log_by_ipv4
}


def _parse_log(text, ip_type):

    ip_parser = IP_TYPE[ip_type]
    res = ip_parser(text)
    if res:
        return res


def parse_log_file(file_path, ip_type=None):
    """
        解析日志文件
    :param file_path: 日志文件路径
    :type file_path: string
    :param ip_type: 指定解析日志的IP类型
    :type ip_type: ipv4 or ipv6
    :return:日志信息生成器
    """
    ip_type = 'IPv4' if ip_type is None else ip_type
    with open(file_path, 'r') as log_fp:
        for log in log_fp:
            yield _parse_log(log, ip_type)