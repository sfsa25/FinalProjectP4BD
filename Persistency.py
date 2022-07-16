# DDL and main database "singleton" connection
import logging
import os
import sqlite3
import PersistencyDDL


class Persistency:

    def __init__(self):
        self.database = "Database/walkclinic.db"
        self.conn = None

    def createtable(self, statement):
        try:
            c = self.pre_statement()
            c.execute(statement)
            self.post_statement()
        except Exception as e:
            logging.error(e)
            raise e

    def setuptables(self):
        for i in PersistencyDDL.list_table:
            self.createtable(i)

    def erasedatabase(self):
        os.remove(self.database)

    def pre_statement(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn.cursor()

    def post_statement(self):
        self.conn.commit()
        self.conn.close()
