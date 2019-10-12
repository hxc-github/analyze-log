# -*- coding: utf-8 -*-
import utils
import report


def main():

    parser_log = utils.Parser()
    logs = parser_log.filter_log_by_type('../test.txt')

    article_reports = report.ArticleReports(logs)
    article_reports.article_report()

    ip_reports = report.IPReports(logs)
    ip_reports.ip_report()

    complete_reports = report.CompleteReports(logs)
    complete_reports.complete_report()


if __name__ == '__main__':

    main()
