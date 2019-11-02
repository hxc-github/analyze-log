# -*- coding: utf-8 -*-
import requests


class HttpClient(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, url):
        url = self.endpoint + url
        res = requests.get(url, timeout=2)
        return res.content
