# -*- coding: utf-8 -*-

ARTICLE_REPORT_ATTRS = ['url', 'title', 'visitors', 'access_ip_num']

IP_REPORT_ATTRS = ['ip', 'visitors', 'article_num']

COMPLETE_REPORT_ATTRS = ['ip', 'url', 'visitors']

REPORT_ATTRS = {
    'article-report': ARTICLE_REPORT_ATTRS,
    'ip-report': IP_REPORT_ATTRS,
    'complete-report': COMPLETE_REPORT_ATTRS
}

ARTICLE_REPORT_ATTRS_DISPLAY = ['URL', '文章标题', '访问人次', '访问IP数']

IP_REPORT_ATTRS_DISPLAY = ['IP', '访问次数', '访问文章数']

COMPLETE_REPORT_ATTRS_DISPLAY = ['IP', 'URL', '访问次数']

REPORT_ATTRS_DISPLAY = {
    'article-report': ARTICLE_REPORT_ATTRS_DISPLAY,
    'ip-report': IP_REPORT_ATTRS_DISPLAY,
    'complete-report': COMPLETE_REPORT_ATTRS_DISPLAY
}

REPORT_NAME = {
    'article-report': '文章报表',
    'ip-report': 'IP报表',
    'complete-report': '完整报表'
}

ARTICLE_TYPES = ['htm', 'html', 'pdf', 'doc', 'docx']
