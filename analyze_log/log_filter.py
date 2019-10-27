# -*- coding: utf-8 -*-
import functools


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
