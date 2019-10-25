# -*- coding: utf-8 -*-
import unittest


class TestBase(unittest.TestCase):

    def setUp(self):
        self.file_path = 'log.txt'
        self.ip = '200.200.1.35'
