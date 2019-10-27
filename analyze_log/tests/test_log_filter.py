# -*- coding: utf-8 -*-
import sys
import os

from base import TestBase
import fake_data
from analyze_log import log_filter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestLogFilter(TestBase):

    def test_log_filter(self):
        """测试滤除日志类型"""
        exp_log = [fake_data.log_dict_html]
        log_list = list()
        log_list.append(fake_data.log_dict_css)
        log_list.append(fake_data.log_dict_html)
        log_gen = (log for log in log_list)
        logs = log_filter.log_filter(log_gen)
        self.assertListEqual(logs, exp_log, '日志滤除失败')

    def test_filter_func_by_type_fail(self):
        self.assertFalse(log_filter._filter_func_by_type(None, ['css']))
