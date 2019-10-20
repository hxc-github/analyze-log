# -*- coding: utf-8 -*-

ARTICLE_TYPES = ['htm', 'html', 'pdf', 'doc', 'docx']


class ReportBase(object):

    def __init__(self, log_list):
        # 列表存放读取的单行日志，为字典结构[{'url':xxx},]
        self.log_list = log_list


# 文章报表
class ArticleReports(ReportBase):

    def __init__(self, log_list, url):
        super(ArticleReports, self).__init__(log_list=log_list)

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

        # 计算IP访问数
        for url, info in report_dict.iteritems():
            info['ip_count'] = len(info['ip_set'])

        return report_dict

    def article_report(self):
        report_dict = self._collect_article_reports()
        print "|URL|文章标题|访问人次|访问IP数|"
        print "|----|-------|-------|--------|"
        for url, info in report_dict.iteritems():
            title = info.get('title')
            access_count = info.get('access_count', None)
            ip_count = info.get('ip_count', None)
            print "|{}|{}|{}|{}|".format(url, title, access_count, ip_count)


# IP报表
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

    def ip_report(self):
        report_dict = self._collect_ip_reports()
        print "|IP|访问次数|访问文章数|"
        print "|----|-------|--------|"
        for ip, info in report_dict.iteritems():
            access_count = info.get('access_count', None)
            article_count = info.get('article_count', None)
            print "|{}|{}|{}|".format(ip, access_count, article_count)


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
            ip_url = ip.join(url)

            # 如果字典里没有包含该IP，则创造个新的字典
            if ip_url in report_dict:
                    report_dict[ip_url]['access_count'] += 1
            else:
                # 构造report为{ip_url:{'access_count':xxx}}
                new_report = {'ip': ip, 'url': url, 'access_count': 1}
                report_dict.update({ip_url: new_report})

        return report_dict

    def complete_report(self):
        report_dict = self._collect_complete_reports()
        print "|IP|URL|访问次数|"
        print "|----|----|------|"
        for ip_url, info in report_dict.iteritems():
            ip = info.get('ip', None)
            url = info.get('url', None)
            access_count = info.get('access_count', None)
            print "|{}|{}|{}|".format(ip, url, access_count)
