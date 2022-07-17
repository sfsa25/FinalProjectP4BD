# DDL and main database "singleton" connection
import logging
import sqlite3

import PersistencyDDL
import pandas as pd

import PersistencyDML


class Persistency:

    def __init__(self):
        self.database = PersistencyDDL.db_path
        self.conn = None

    def pre_statement(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn.cursor()

    def post_statement(self):
        self.conn.commit()
        self.conn.close()

    def execute_command(self, statement):
        try:
            c = self.pre_statement()
            c.execute(statement)
            self.post_statement()
        except Exception as e:
            logging.error(e)
            raise e

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

    # create = 1
    # drop   = 0
    def setup_tables(self, create_or_drop):
        list_to_use = ''
        if create_or_drop:
            list_to_use = PersistencyDDL.list_create_table
        else:
            list_to_use = PersistencyDDL.list_drop_table
        try:
            for i in list_to_use:
                self.execute_command(i)
        except Exception as e:
            raise e


    def setup_data(self):
        try:
            for i in PersistencyDML.list_initial_data:
                self.execute_command(i)
        except Exception as e:
            raise e
