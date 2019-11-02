# -*- coding: utf-8 -*-
import logging
from abc import abstractmethod

import exc
from common import contants
from common.contants import DB_NAME
from common.contants import PAGE_FILE_TYPES
import title

LOG = logging.getLogger(__name__)


class ReportBase(object):

    def __init__(self, log_list):
        # 列表存放读取的单行日志，为字典结构[{'url':xxx},]
        self.log_list = log_list
        self.reports = dict()

    @abstractmethod
    def gen_reports(self):
        """生成报表"""


# 文章报表
class ArticleReports(ReportBase):

    def __init__(self, log_list, ip):
        self.ip = ip
        self.sql = title.TitleSql(DB_NAME)
        super(ArticleReports, self).__init__(log_list=log_list)

    def _calculate_ip_num(self, report):
        """
            计算IP访问数
        :param report:
        :return:
        """
        for url, info in report.iteritems():
            info['access_ip_num'] = len(info['ip_set'])

        return report

    def _set_title(self, report):
        for url, info in report.iteritems():
            if url.split('.')[-1] not in PAGE_FILE_TYPES:
                info['title'] = 'No title'
                continue
            info['title'] = self.sql.read_title(self.ip, url)
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
            for article_type in contants.ARTICLE_TYPES:
                if not url.endswith(article_type):
                    continue

                # 如果字典里没有包含该URL，则创造个新的字典
                if url in report_dict:
                    report_dict[url]['visitors'] += 1
                    report_dict[url]['ip_set'].add(ip)

                else:
                    ip_set = {ip}

                    # 构造report为{url:{'title':xxx}}
                    new_report = {'title': '', 'visitors': 1, 'url': url,
                                  'ip_set': ip_set, 'access_ip_num': 1}
                    report_dict.update({url: new_report})

        return report_dict

    def gen_reports(self):
        # 1、收集文章报表
        report_dict = self._collect_article_reports()

        # 2、计算文章报表IP访问数
        report_dict = self._calculate_ip_num(report_dict)

        # 3、获取文章title
        report_dict = self._set_title(report_dict)

        self.reports = report_dict
        return report_dict


class IPReports(ReportBase):

    def __init__(self, log_list):
        super(IPReports, self).__init__(log_list=log_list)

    def gen_reports(self):
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
                report_dict[ip]['visitors'] += 1

                # 循环遍历文章类型
                for article_type in contants.ARTICLE_TYPES:
                    if not url.endswith(article_type):
                        continue
                    report_dict[ip]['article_num'] += 1
            else:
                # 构造report为{ip:{'access_count':xxx}}
                new_report = {'ip': ip, 'article_num': 0, 'visitors': 1}
                for article_type in contants.ARTICLE_TYPES:
                    if not url.endswith(article_type):
                        continue
                    new_report['article_num'] += 1
                report_dict.update({ip: new_report})

        return report_dict


# 完整报表
class CompleteReports(ReportBase):

    def __init__(self, log_list):
        super(CompleteReports, self).__init__(log_list=log_list)

    def gen_reports(self):
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
                    report_dict[ip_url]['visitors'] += 1
            else:
                # 构造report为{ip_url:{'access_count':xxx}}
                new_report = {'ip': ip, 'url': url, 'visitors': 1}
                report_dict.update({ip_url: new_report})

        return report_dict


REPORT_TYPES = {
    'article-report': ArticleReports,
    'ip-report': IPReports,
    'complete-report': CompleteReports
}


def get_report_obj(logs, report_type, **kwargs):
    assert logs
    assert report_type

    if report_type == 'article-report':
        ip = kwargs.get('ip', None)
        return ArticleReports(logs, ip)
    elif report_type in REPORT_TYPES:
        return REPORT_TYPES[report_type](logs)
    else:
        LOG.error('The report type entered is: %s, which is not currently'
                  ' supported.' % report_type)
        raise exc.ReportTypeError('输入的报表类型是：%s，暂时不支持该类型' %
                                  report_type)
