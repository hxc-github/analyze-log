# -*- coding: utf-8 -*-
import sys
import os
import mock

from analyze_log.common import http
from base import TestBase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class Response(object):
    content = 'test'


class TestHttp(TestBase):

    def setUp(self):
        super(TestHttp, self).setUp()

    @mock.patch('analyze_log.common.http.requests.get')
    def test_http_get(self, get_mock):
        get_mock.return_value = Response
        act_content = http.HttpClient(self.endpoint).get(self.url)
        exp_content = 'test'
        self.assertEqual(act_content, exp_content, 'http get测试失败')
