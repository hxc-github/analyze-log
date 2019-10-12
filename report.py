# -*- coding: utf-8 -*-


class ReportBase(object):

    def __init__(self, log_list):
        self.log_list = log_list


# 文章报表
class ArticleReports(ReportBase):

    def __init__(self, log_list):
        self.article_types = ['htm', 'html', 'pdf', 'doc', 'docx']
        super.__init__(log_list=log_list)

    def _collect_article_reports(self):

        for log in self.log_list:
            url = log.get('url')
            ip = log.get('ip')

            for article_type in self.article_types:
                report_dict = dict()
                if article_type not in url:
                    continue
                report_dict[url]['count'] += 1
                if url in report_dict:
                    report_dict[url]['count'] += 1
                    if ip not in report_dict[url]['ip_list']:
                        report_dict[url]['ip_list'].append(ip)

                else:
                    ip_list = [ip]
                    new_report = {'title': '', 'count': 1,
                                  'ip_list': ip_list, 'ip_count': 1}
                    report_dict.update({url: new_report})
        return report_dict

    def article_report(self):
        report_dict = self._collect_article_reports()
        print "|URL|文章标题|访问人次|访问IP数|"
        print "|----|-------|-------|--------|"
