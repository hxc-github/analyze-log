# -*- coding: utf-8 -*-
import utils
import report

def main():

    fil = utils.Filter()
    logs = fil.filter_log_by_type('test.txt')
    article_reports = report.ArticleReports(logs)
    article_reports.article_report()


if __name__ == '__main__':

    main()
