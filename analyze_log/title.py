# -*- coding: utf-8 -*-
import logging

from common import sql
from common import http
from common import utils
from common.contants import TITLE_TABLE_NAME
from common.contants import PAGE_FILE_TYPES
import exc

LOG = logging.getLogger(__name__)

WRITE_CMD = 'INSERT INTO title (ip,url,title) VALUES ("{0}", "{1}", "{2}");'

READ_CMD = 'SELECT title FROM {0} WHERE ip="{1}"  AND url="{2}";'

CREAD_TABLE_CMD = 'CREATE TABLE {0}' \
            '(ip CHAR(20),' \
            'url CHAR(50) ,' \
            'title VARCHAR(100),' \
            ' PRIMARY KEY (ip, url));'

DEL_TABLE_CMD = 'DROP TABLE IF EXISTS {0}'


class TitleSql(sql.SqlBase):

    def __init__(self, db_name):
        assert db_name
        super(TitleSql, self).__init__(db_name)

    def _create_table(self):
        cmd = CREAD_TABLE_CMD.format(TITLE_TABLE_NAME)
        self._exec_cmd(cmd)

    def _del_table(self):
        cmd = DEL_TABLE_CMD.format(TITLE_TABLE_NAME)
        self._exec_cmd(cmd)

    def check_table(self):
        self._del_table()
        self._create_table()

    def write_table(self, ip, url, title):
        write_cmd = WRITE_CMD.format(ip, url, title)
        self._exec_cmd(write_cmd)

    def read_table(self, ip, url):
        read_cmd = READ_CMD.format(TITLE_TABLE_NAME, ip, url)
        title_iter = self._exec_cmd(read_cmd)
        try:
            (title,) = title_iter.fetchone()
        except Exception:
            return 'No title'
        return title


class KeepTitle(object):

    def __init__(self, db_name, logs, ip):
        assert db_name
        assert ip
        assert logs
        self.ip = ip
        self.logs = logs
        endpoint = 'http://' + self.ip
        self.http_client = http.HttpClient(endpoint)
        self.sql_client = TitleSql(db_name)
        self.sql_client.check_table()

    def _fecth_content_from_web(self, url):
        log_type = url.split('.')[-1]
        if log_type not in PAGE_FILE_TYPES:
            return 'No title'
        try:
            return r'<title>succeed</title>'
            content = self.http_client.get(url)
        except Exception:
            LOG.exception('HTTP请求失败')
            raise exc.HTTPError('HTTP请求失败')
        return content

    def keep_title_to_sql(self):
        print 'start to keep title'
        for info in self.logs:
            if not info:
                continue
            if not info['url']:
                continue
            if info['url'].split('.')[-1] not in PAGE_FILE_TYPES:
                continue
            content = self._fecth_content_from_web(info['url'])
            title = utils.get_html_title(content)
            self.sql_client.write_table(self.ip, info['url'], title)
        print 'keep title to sql complete'
