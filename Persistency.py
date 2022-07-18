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

    def execute_transaction(self, statement):
        try:
            c = self.pre_statement()
            c.execute(PersistencyDML.begin_transaction)
            for st in statement:
                c.execute(st)
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
            logging.error("WAS NOT POSSIBLE TO SETUP TABLES")
            raise e

    def setup_data(self):
        try:
            for i in PersistencyDML.list_initial_data:
                self.execute_command(i)
        except Exception as e:
            logging.error("WAS NOT POSSIBLE TO LOAD INITIAL DATA INTO THE TABLES")
            raise e

    def insert_doctor_trans(self, doctor):
        statements = [
            PersistencyDML.insert_user + "'" + doctor.user.login + "','" + doctor.user.passwd + "', '" + doctor.user.role + "')",
            PersistencyDML.insert_doctor + "(SELECT MAX(ID) FROM USER), " + doctor.specialty + ")"]
        self.execute_transaction(statements)

    def findDoctor(self, doctor):
        self.findUser(doctor.user)
        result_doctor = self.execute_select(PersistencyDML.select_all_doctor + " WHERE USERID = " + str(doctor.user.id))
        doctor.specialty = result_doctor[0][2]
        return doctor;

    def findUser(self, user):
        result_user = self.execute_select(PersistencyDML.select_all_user + " WHERE LOGIN = '" + user.login + "'")
        user.id = result_user[0][0]
        user.role = result_user[0][2]