from .database import Database
import sqlite3

class Sqlite3Database(Database):
    def __init__(self, db_name : str):
        self.__db_name = db_name
    
    def execute(self, command : str):
        con = sqlite3.connect(self.__db_name)
        cursor = con.cursor()
        cursor.execute(command)
        con.commit()
        con.close()