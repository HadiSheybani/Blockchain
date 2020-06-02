import pytest
from hamcrest import *
import sqlite3
import os

from framework.sqlite3db import Sqlite3Database
from entity.block import Block

class TestSqlite3Database:
    def setup_method(self):
        self.__db_name = 'test.db'
        self.__db_create = False
        self.__db = Sqlite3Database(self.__db_name)

    def teardown_method(self):
        if self.__db_create:
            self.__con.close()
        os.remove(self.__db_name)

    def __connect_db(self):
        self.__con = sqlite3.connect(self.__db_name)
        self.__db_create = True
        self.__cursor = self.__con.cursor()

    def __create_table(self):
        create_command = """CREATE TABLE IF NOT EXISTS BlockChain 
                            ("index", "time", "data", "pre hash", "block hash")"""
        self.__db.execute(create_command)

    def test_GivenCreateTableCommandWhenCallExecuteThenItShouldCreateTable(self):
        self.__create_table()
        self.__connect_db()
        self.__cursor.execute('SELECT name from sqlite_master where type= "table"')
        data = self.__cursor.fetchall()
        assert_that(len(data), equal_to(1))
        assert_that(data[0][0], equal_to('BlockChain'))

    def test_GivenInsertDataCommandWhenCallExecuteThenItShouldAddDataIntoTable(self):
        self.__create_table()
        insert_command = """INSERT INTO BlockChain 
                            ("index", "time", "data", "pre hash", "block hash") 
                            VALUES (1, 1000, "first block", "pre_hash", "block_hash")"""
        self.__db.execute(insert_command)
        self.__connect_db()
        self.__cursor.execute('''SELECT * from BlockChain''')
        data = self.__cursor.fetchall()
        assert_that(data, equal_to([(1, 1000, "first block", "pre_hash", "block_hash")]))

