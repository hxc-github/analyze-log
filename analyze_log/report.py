# -*- coding: utf-8 -*-
import re
import logging

import exc
import utils
import http

LOG = logging.getLogger(__name__)

ARTICLE_TYPES = ['htm', 'html', 'pdf', 'doc', 'docx', 'icon']

IP = None


class ReportBase(object):

    def __init__(self, log_list):
        # 列表存放读取的单行日志，为字典结构[{'url':xxx},]
        self.log_list = log_list
        self.reports = dict()


# 文章报表
class ArticleReports(ReportBase):

    def __init__(self, log_list):
        self.ip = IP
        super(ArticleReports, self).__init__(log_list=log_list)

    def _calculate_ip_num(self, report):
        """
            计算IP访问数
        :param report:
        :return:
        """
        for url, info in report.iteritems():
            info['ip_count'] = len(info['ip_set'])

        return report

    def _set_title(self, report):
        endpoint = 'http://' + self.ip
        http_client = http.HttpClient(endpoint)

        for url, info in report.iteritems():
            log_type = url.split('.')[-1]

            if log_type == 'html' or log_type == 'htm':
                try:
                    content = http_client.get(url)
                except Exception:
                    LOG.exception('HTTP请求失败')
                    raise exc.HTTPError('HTTP请求失败')

                title = http.get_html_title(content)
                info['title'] = title
        return report

    def _collect_article_reports(self):
        """
            收集文章报表
        :return:
        """
        # 通过遍历日志列表，按照文章类型进行筛选
        report_dict = dict()
        for log in self.log_list:
            url = log.get('url')
            ip = log.get('ip')
            for article_type in ARTICLE_TYPES:
                if not url.endswith(article_type):
                    continue

                # 如果字典里没有包含该URL，则创造个新的字典
                if url in report_dict:
                    report_dict[url]['access_count'] += 1
                    report_dict[url]['ip_set'].add(ip)

                else:
                    ip_set = {ip}

                    # 构造report为{url:{'title':xxx}}
                    new_report = {'title': '', 'access_count': 1,
                                  'ip_set': ip_set, 'ip_count': 1}
                    report_dict.update({url: new_report})

        return report_dict

    def _display(self):
        print "|URL|文章标题|访问人次|访问IP数|"
        print "|----|-------|-------|--------|"
        for url, info in self.reports.iteritems():
            title = info.get('title')
            access_count = info.get('access_count', None)
            ip_count = info.get('ip_count', None)
            print "|{}|{}|{}|{}|".format(url, title, access_count, ip_count)

    def get_reports(self):
        # 1、收集文章报表
        report_dict = self._collect_article_reports()

        # 2、计算文章报表IP访问数
        report_dict = self._calculate_ip_num(report_dict)

        # 3、获取文章title
        report_dict = self._set_title(report_dict)

        self.reports = report_dict

        # 4、打印文章报表
        self._display()


class IPReports(ReportBase):

    def __init__(self, log_list):
        super(IPReports, self).__init__(log_list=log_list)

    def _collect_ip_reports(self):
        """
            收集IP报表
        :return:
        """
        # 通过遍历日志列表，按照IP进行筛选
        report_dict = dict()
        for log in self.log_list:
            ip = log.get('ip')
            url = log.get('url')
            # 如果字典里没有包含该IP，则创造个新的字典
            if ip in report_dict:
                report_dict[ip]['access_count'] += 1

                # 循环遍历文章类型
                for article_type in ARTICLE_TYPES:
                    if not url.endswith(article_type):
                        continue
                    report_dict[ip]['article_count'] += 1
            else:
                # 构造report为{ip:{'access_count':xxx}}
                new_report = {'article_count': 0, 'access_count': 1}
                for article_type in ARTICLE_TYPES:
                    if not url.endswith(article_type):
                        continue
                    new_report['article_count'] += 1
                report_dict.update({ip: new_report})

        return report_dict

    def _display(self):
        print "|IP|访问次数|访问文章数|"
        print "|----|-------|--------|"
        for ip, info in self.reports.iteritems():
            access_count = info.get('access_count', None)
            article_count = info.get('article_count', None)
            print "|{}|{}|{}|".format(ip, access_count, article_count)

    def get_reports(self):
        # 1、获取IP报表
        self.reports = self._collect_ip_reports()

        # 2、打印IP报表
        self._display()


# 完整报表
class CompleteReports(ReportBase):

    def __init__(self, log_list):
        super(CompleteReports, self).__init__(log_list=log_list)

    def _collect_complete_reports(self):
        """
            收集完整报表
        :return:
        """
        # 通过遍历日志列表，按照IP和URL进行筛选
        report_dict = dict()
        for log in self.log_list:
            ip = log.get('ip')
            url = log.get('url')
            ip_url = ip + url

            # 如果字典里没有包含该IP，则创造个新的字典
            if ip_url in report_dict:
                    report_dict[ip_url]['access_count'] += 1
            else:
                # 构造report为{ip_url:{'access_count':xxx}}
                new_report = {'ip': ip, 'url': url, 'access_count': 1}
                report_dict.update({ip_url: new_report})

        return report_dict

    def _display(self):
        print "|IP|URL|访问次数|"
        print "|----|----|------|"
        for ip_url, info in self.reports.iteritems():
            ip = info.get('ip', None)
            url = info.get('url', None)
            access_count = info.get('access_count', None)
            print "|{}|{}|{}|".format(ip, url, access_count)

    def get_reports(self):
        # 1、收集完整报表
        self.reports = self._collect_complete_reports()

        # 2、打印完整报表
        self._display()


REPORT_TYPES = {
    'article-report': ArticleReports,
    'ip-report': IPReports,
    'complete-report': CompleteReports
}


def _report(logs, report_type, ip=None):
    assert logs
    assert report_type

    if report_type in REPORT_TYPES:
        return REPORT_TYPES[report_type](logs)
    else:
        LOG.error('The report type entered is: %s, which is not currently'
                  ' supported.' % report_type)
        raise exc.ReportTypeError('输入的报表类型是：%s，暂时不支持该类型' %
                                  report_type)


def display_report(file_path, report_type, filter_types=None, ip=None):
    assert file_path
    assert report_type
    global IP

    IP = ip
    logs = utils.parse_log_file(file_path)
    logs = utils.log_filter(logs, filter_types)

    reports = _report(logs, report_type, ip)
    reports.get_reports()
