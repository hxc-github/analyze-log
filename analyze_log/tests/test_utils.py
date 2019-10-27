# -*- coding: utf-8 -*-
import sys
import os

from base import TestBase
from analyze_log.common import utils
import fake_data
from analyze_log.common import contants

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestUtils(TestBase):

    def setUp(self):
        super(TestUtils, self).setUp()

    def test_get_html_title_succeed(self):
        response = fake_data.title
        act_title = utils.get_html_title(response)
        exp_title = 'test analyze log'
        self.assertEqual(act_title, exp_title, '获取title失败')

    def test_get_html_title_fail(self):
        response = 'test'
        act_title = utils.get_html_title(response)
        exp_title = ''
        self.assertEqual(act_title, exp_title, '获取title不一致')

    def test_transform_to_list(self):
        report_dict = fake_data.ip_report
        report_type = self.ip_report_type
        act_report = utils.transform_to_list(report_dict, report_type)
        exp_report = fake_data.ip_attrs
        self.assertListEqual(act_report, exp_report)

    def test_display_by_markdown(self):
        table_name = 'table'
        attr_names = contants.ARTICLE_REPORT_ATTRS_DISPLAY
        attrs = fake_data.ip_attrs
        act = utils.display_by_markdown(table_name, attr_names, attrs)
        self.assertIsNone(act)
