# -*- coding: utf-8 -*-
import requests
import re


class HttpClient(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, url):
        url = self.endpoint + url
        res = requests.get(url)
        return res.content()


def get_html_title(response):
    # 正则表达式匹配标题
    pat = r'<title>(?P<title>.*?)</title>'
    res = re.search(pat, str(response))
    if not res:
        return ''
    title = res.groupdict()['title']
    return title
