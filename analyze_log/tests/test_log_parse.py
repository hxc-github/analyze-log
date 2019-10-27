# -*- coding: utf-8 -*-
import mock
import sys
import os

from base import TestBase
from collections import Iterable
from analyze_log import log_parse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestLogParse(TestBase):

    @mock.patch('analyze_log.log_parse.open', mock.mock_open(
        read_data='200.200.76.130 - - [16/Feb/2019:11:27:20 +0800] '
                  '"GET /coding/miniproject/material.html HTTP/1.1" 200 38093')
                )
    def test_parse_log_file_by_type(self, ):
        """测试是否是可迭代对象"""
        logs = log_parse.parse_log_file(self.file_path)
        self.assertIsInstance(tuple(logs), Iterable, '不是可迭代对象')
