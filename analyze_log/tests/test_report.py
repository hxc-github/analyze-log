# -*- coding: utf-8 -*-
import mock
import sys
import os

from base import TestBase
from analyze_log import report
import fake_data
from analyze_log import exc

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestReport(TestBase):

    def setUp(self):
        super(TestReport, self).setUp()

    def test_calculate_ip_num(self):
        """测试计算IP访问数"""
        reports = fake_data.article_report_dict
        exp_report = fake_data.ip_num_report
        article = report.ArticleReports([], self.ip)
        self.assertIsInstance(article, report.ArticleReports, '返回文章类错误')
        act_report = article._calculate_ip_num(reports)
        self.assertDictEqual(act_report, exp_report, '计算访问数错误')

    @mock.patch('analyze_log.common.http.HttpClient.get')
    def test_set_title(self, res_mock):
        """测试设置标题"""
        res_mock.return_value = fake_data.title
        reports = fake_data.article_report_dict
        exp_report = fake_data.title_report
        article = report.ArticleReports([], self.ip)
        self.assertIsInstance(article, report.ArticleReports, '返回文章类错误')
        act_report = article._set_title(reports)
        self.assertDictEqual(act_report, exp_report, '设置标题失败')

    def test_collect_article_reports(self):
        """测试收集文章报表"""
        article = report.ArticleReports(fake_data.log_list, self.ip)
        self.assertIsInstance(article, report.ArticleReports, '返回文章类错误')
        exp_report = fake_data.article_report_no_ip_num
        act_report = article._collect_article_reports()
        self.assertDictEqual(act_report, exp_report, '收集文章报表失败')

    def test_collect_ip_reports(self):
        """测试收集IP报表"""
        ip_report = report.IPReports(fake_data.log_list)
        self.assertIsInstance(ip_report, report.IPReports, '返回文章类错误')
        act_report = ip_report.gen_reports()
        exp_report = fake_data.ip_report
        self.assertDictEqual(act_report, exp_report, '收集IP报表错误')

    def test_collect_complete_reports(self):
        """测试收集完整报表"""
        complete_report = report.CompleteReports(fake_data.log_list)
        self.assertIsInstance(complete_report, report.CompleteReports,
                              '返回完整报表类错误')
        act_report = complete_report.gen_reports()
        exp_report = fake_data.complete_report
        self.assertDictEqual(act_report, exp_report, '收集完整报表错误')

    def test_input_article_report(self):
        """测试传入文章报表请求"""
        report_type = 'article-report'
        act_report = report.get_report_obj(fake_data.log_list, report_type)
        self.assertIsInstance(act_report, report.ArticleReports,
                              '文章报表初始化失败')

    def test_input_ip_report(self):
        """测试传入IP报表请求"""
        report_type = 'ip-report'
        act_report = report.get_report_obj(fake_data.log_list, report_type)
        self.assertIsInstance(act_report, report.IPReports,
                              'IP报表初始化失败')

    def test_input_complete_report(self):
        """测试传入完整报表请求"""
        report_type = 'complete-report'
        act_report = report.get_report_obj(fake_data.log_list, report_type)
        self.assertIsInstance(act_report, report.CompleteReports,
                              '完整报表初始化失败')

    def test_input_other_report(self):
        """测试传入其他类型报表请求"""
        report_type = 'inexistence-report'
        info = {'report_type': report_type, 'logs': fake_data.log_list}
        self.assertRaises(exc.ReportTypeError, report.get_report_obj, **info)
