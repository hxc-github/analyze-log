# -*- coding: utf-8 -*-


class LogExceptionBase(Exception):

    def __init__(self, message):
        self.message = message
        super(LogExceptionBase, self).__init__(self, message)

    def __str__(self):
        return self.message


class IpFormatError(LogExceptionBase):
    pass


class ReportTypeError(LogExceptionBase):
    pass
