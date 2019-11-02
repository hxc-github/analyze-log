# -*- coding: utf-8 -*-


class LogExceptionBase(Exception):
    pass


class IpFormatError(LogExceptionBase):
    pass


class ReportTypeError(LogExceptionBase):
    pass


class IpTypeError(LogExceptionBase):
    pass


class HTTPError(LogExceptionBase):
    pass


class FuncDontSupport(LogExceptionBase):
    pass
