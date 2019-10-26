# -*- coding: utf-8 -*-
import mock
import sys
import os
from collections import Iterable

from base import TestBase
from analyze_log import utils
import fake_data

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestUtils(TestBase):

    def setUp(self):
        super(TestUtils, self).setUp()

    @mock.patch('analyze_log.utils.open', mock.mock_open(
        read_data='200.200.76.130 - - [16/Feb/2019:11:27:20 +0800] '
                  '"GET /coding/miniproject/material.html HTTP/1.1" 200 38093')
                )
    def test_parse_log_file_by_type(self, ):
        """测试是否是可迭代对象"""
        act_log = ({
            'content_length': '38093', 'code': '200',
            'protocol': 'HTTP/1.1',
            'url': '/coding/miniproject/material.html',
            'ip': '200.200.76.130',
            'datetime': '16/Feb/2019:11:27:20 +0800',
            'method': 'GET'
        },)
        logs = utils.parse_log_file(self.file_path)
        self.assertIsInstance(tuple(logs), Iterable, '不是可迭代对象')

    def test_log_filter(self):
        """测试滤除日志类型"""
        exp_log = [fake_data.log_dict_html]
        log_list = list()
        log_list.append(fake_data.log_dict_css)
        log_list.append(fake_data.log_dict_html)
        log_gen = (log for log in log_list)
        logs = utils.log_filter(log_gen)
        self.assertListEqual(logs, exp_log, '日志滤除失败')
