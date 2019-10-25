# -*- coding: utf-8 -*-
import mock
import sys
import os

from analyze_log import http
from base import TestBase
from analyze_log import exc
import fake_data

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestHttp(TestBase):

    def setUp(self):
        super(TestHttp, self).setUp()

    def test_get_html_title_succeed(self):
        response = fake_data.title
        act_title = http.get_html_title(response)
        exp_title = 'test analyze log'
        self.assertEqual(act_title, exp_title, '获取title失败')

    def test_get_html_title_fail(self):
        response = 'test'
        act_title = http.get_html_title(response)
        exp_title = ''
        self.assertEqual(act_title, exp_title, '获取title不一致')
