# -*- coding: utf-8 -*-


class LogExceptionBase(Exception):
    pass


class IpFormatError(LogExceptionBase):
    pass


class ReportTypeError(LogExceptionBase):
    pass


class IpTypeError(LogExceptionBase):
    message = 'IP类型必须是String类型，输入的IP类型是：%s'


class HTTPError(LogExceptionBase):
    pass


class FuncDontSupport(LogExceptionBase):
    pass
