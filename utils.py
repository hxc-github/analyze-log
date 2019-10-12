# -*- coding: utf-8 -*-


def read_log_file(file_path):
    """
        读取日志文件
    :param file_path: 日志文件路径
    :return: 返回日志文件列表
    """

    # TODO: 异常处理未做
    log_list = []
    mode = 'r+'
    with open(file_path, mode) as log_fp:
        while True:
            log_buf = log_fp.readline()
            if not log_buf:
                break
            log_list.append(log_buf)
    return log_list
