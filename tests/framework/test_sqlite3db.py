import pytest
from hamcrest import *
import sqlite3
import os

from framework.sqlite3db import Sqlite3Database

class TestSqlite3Database:
    def setup_method(self):
        self.__db_name = 'test.db'
        self.__db_create = False

    def teardown_method(self):
        if self.__db_create:
            self.__con.close()
        os.remove(self.__db_name)

    def __connect_db(self):
        self.__con = sqlite3.connect(self.__db_name)
        self.__db_create = True
        self.__cursor = self.__con.cursor()

    def test_GivenCreateTableCommandWhenCallExecuteThenItShouldCreateTable(self):
        command = 'CREATE TABLE BlockChain ("index" "time stamp" "data" "pre hash" "block hash")'
        db = Sqlite3Database(self.__db_name)
        db.execute(command)
        self.__connect_db()
        self.__cursor.execute('SELECT name from sqlite_master where type= "table"')
        data = self.__cursor.fetchall()
        assert_that(len(data), equal_to(1))
        assert_that(data[0][0], equal_to('BlockChain'))
