# -*- coding: utf-8 -*-

ARTICLE_TYPE = ['htm', 'html', 'pdf', 'doc', 'docx']


class ReportBase(object):

    def __init__(self, log_list):
        self.log_list = log_list


# 文章报表
class ArticleReports(ReportBase):

    def __init__(self, log_list):
        super(ArticleReports, self).__init__(log_list=log_list)

    def _collect_article_reports(self):
        """
            收集文章报表
        :return:
        """
        # 通过遍历日志列表，按照文章类型进行筛选
        # 列表存放读取的单行日志，为字典结构
        report_dict = dict()
        for log in self.log_list:
            url = log.get('url')
            ip = log.get('ip')
            for article_type in ARTICLE_TYPE:
                if article_type not in url:
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
