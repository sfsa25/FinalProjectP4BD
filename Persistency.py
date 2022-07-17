# DDL and main database "singleton" connection
import logging
import os
import sqlite3
import PersistencyDDL
import pandas as pd


class Persistency:

    def __init__(self):
        self.database = "Database/walkclinic.db"
        self.conn = None

    def execute_command(self, statement):
        try:
            c = self.pre_statement()
            c.execute(statement)
            self.post_statement()
        except Exception as e:
            logging.error(e)
            raise e

    def setup_tables(self):
        for i in PersistencyDDL.list_table:
            self.execute_command(i)

    def erase_database(self):
        os.remove(self.database)

    def pre_statement(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn.cursor()

    def post_statement(self):
        self.conn.commit()
        self.conn.close()

    def execute_select(self, statement):
        try:
            c = self.pre_statement()
            c.execute(statement)
            return c.fetchall()
        except Exception as e:
            logging.error(e)
            raise e

    def execute_select_pandas(self, statement):
        try:
            c = self.pre_statement()
            df = pd.read_sql_query(statement, self.conn)
            self.conn.close()
            return df
        except Exception as e:
            logging.error(e)
            raise e


