# -*- coding: utf-8 -*-
import sys
import os
import mock

from analyze_log import http
from base import TestBase
import fake_data

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class Response(object):
    content = 'test'


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

    @mock.patch('analyze_log.http.requests.get')
    def test_http_get(self, get_mock):
        get_mock.return_value = Response
        act_content = http.HttpClient(self.endpoint).get(self.url)
        exp_content = 'test'
        self.assertEqual(act_content, exp_content, 'http get测试失败')
