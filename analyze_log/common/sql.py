# -*- coding: utf-8 -*-
import sqlite3


class SqlBase(object):

    def __init__(self, db_name):
        assert db_name
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def _exec_cmd(self, cmd):
        result = self.cursor.execute(cmd)
        self.db.commit()
        return result
