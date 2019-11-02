# -*- coding: utf-8 -*-
import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.file_path = 'log.txt'
        self.ip = '200.200.1.35'
        self.endpoint = 'http://200.200.1.35'
        self.url = '/test.html'
        self.doc_url = '/test.doc'
        self.ip_report_type = 'ip-report'
        self.title = 'title test'
        self.no_title = 'No title'
        self.web_title = '<title>title test</title>'
        self.db_name = 'test.db'
