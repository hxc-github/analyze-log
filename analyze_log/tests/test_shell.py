# -*- coding: utf-8 -*-


import sys
import os

from base import TestBase
from analyze_log import shell

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestShell(TestBase):

    def setUp(self):
        super(TestShell, self).setUp()

    def test_init_args(self):
        sys.argv.append('--file-path=log.txt')
        sys.argv.append('--report-type=ip-report')
        sys.argv.append('--filter-types=css')
        sys.argv.append('--ip=200.200.1.35')
        args = shell.init_args()
        act_args = (args.file_path, args.report_type, args.filter_types, args.ip)  # noqa: E501
        exp_args = ('log.txt', 'ip-report', ["css"], '200.200.1.35')
        self.assertTupleEqual(act_args, exp_args, '参数不匹配')
