# -*- coding: utf-8 -*-
import sys
import os
import mock
from sqlalchemy.exc import IntegrityError

from base import TestBase
from analyze_log import title
from analyze_log import exc
from analyze_log.common import utils
import fake_data
from analyze_log.common import contants

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestTitle(TestBase):

    def setUp(self):
        super(TestTitle, self).setUp()
        self.logs = fake_data.log_list
        self.logs.append(None)
        self.logs.append(fake_data.log_no_url)
        self.title_sql = title.TitleSql(self.db_name)

    @mock.patch('analyze_log.common.sql.SqlBase._exec_cmd')
    def test_check_table(self, res_mock):
        res_mock.return_value = None
        act_res = self.title_sql.check_table()
        self.assertIsNone(act_res)

    @mock.patch('analyze_log.common.sql.SqlBase._exec_cmd')
    def test_write_table(self, res_mock):
        res_mock.return_value = None
        act_res = self.title_sql.write_table(self.ip, self.url, self.title)
        self.assertIsNone(act_res)

    @mock.patch('analyze_log.common.sql.SqlBase._exec_cmd')
    def test_read_title(self, res_mock):
        res_mock.return_value = fake_data.ReadTitle()
        act_res = self.title_sql.read_title(self.ip, self.url)
        exp_res = self.title
        self.assertEqual(act_res, exp_res)

    @mock.patch('analyze_log.common.sql.SqlBase._exec_cmd')
    def test_read_title_error(self, res_mock):
        res_mock.return_value = fake_data.ReadTitleError()
        act_res = self.title_sql.read_title(self.ip, self.url)
        exp_res = self.no_title
        self.assertEqual(act_res, exp_res)

    @mock.patch('analyze_log.common.http.HttpClient.get')
    @mock.patch('analyze_log.title.TitleSql.check_table')
    def test_fetch_content_from_web(self, check_mock, get_mock):
        check_mock.return_value = None
        get_mock.return_value = self.web_title

        keep_title = title.KeepTitle(self.db_name, fake_data.log_list, self.ip)
        act_content = keep_title._fecth_content_from_web(self.url)
        exp_content = self.web_title
        self.assertEqual(act_content, exp_content)

    @mock.patch('analyze_log.common.http.HttpClient.get')
    @mock.patch('analyze_log.title.TitleSql.check_table')
    def test_fetch_content_from_web_error(self, check_mock, get_mock):
        check_mock.return_value = None
        get_mock.side_effect = Exception

        keep_title = title.KeepTitle(self.db_name, fake_data.log_list, self.ip)

        self.assertRaises(exc.HTTPError, keep_title._fecth_content_from_web,
                          url=self.url)

    @mock.patch('analyze_log.title.TitleSql.check_table')
    def test_fetch_content_from_web_no_type(self, check_mock):
        check_mock.return_value = None
        keep_title = title.KeepTitle(self.db_name, fake_data.log_list, self.ip)
        act_res = keep_title._fecth_content_from_web(self.doc_url)
        exp_res = 'No title'
        self.assertEqual(act_res, exp_res)

    @mock.patch('analyze_log.title.TitleSql.write_table')
    @mock.patch('analyze_log.title.KeepTitle._fecth_content_from_web')
    @mock.patch('analyze_log.common.utils.get_html_title')
    @mock.patch('analyze_log.title.TitleSql.check_table')
    def test_keep_title_to_sql(self, check_mock, title_mock, content_mock,
                               write_mock):
        check_mock.return_value = None
        title_mock.return_value = self.title
        content_mock.return_value = self.web_title
        write_mock.return_value = None

        keep_title = title.KeepTitle(self.db_name, self.logs, self.ip)
        act_res = keep_title.keep_title_to_sql()
        self.assertIsNone(act_res)

    def tearDown(self):
        # if os.path.exists('test.db'):
        pass
        #os.system('rm -rf ../test.db')
