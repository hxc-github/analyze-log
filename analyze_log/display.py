# -*- coding: utf-8 -*-
import report
import utils
import logging
import exc

LOG = logging.getLogger(__name__)


class DisplayReport(object):

    def __init__(self, file_path, report_type, filter_types, ip):
        assert file_path
        assert report_type

        self.file_path = file_path
        self.report_type = report_type
        self.filter_types = filter_types
        self.ip = ip

        parser_log = utils.Parser()
        self.logs = parser_log.filter_log_by_type(file_path, filter_types)

    def get(self):

        if self.report_type == 'article-report':
            article_reports = report.ArticleReports(self.logs, self.ip)
            article_reports.article_report()
        elif self.report_type == 'ip-report':
            ip_reports = report.IPReports(self.logs)
            ip_reports.ip_report()
        elif self.report_type == 'complete-report':
            complete_reports = report.CompleteReports(self.logs)
            complete_reports.complete_report()
        else:
            LOG.error('The report type entered is: %s, which is not currently'
                      ' supported.' % self.report_type)
            exc.ReportTypeError('输入的报表类型是：%s，暂时不支持该类型' %
                                self.report_type)
