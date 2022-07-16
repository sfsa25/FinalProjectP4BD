# DDL and main database "singleton" connection
import logging
import os
import sqlite3
from os.path import exists as file_exists
import PersistencyDDL


class Persistency:
    conn = 0

    def __init__(self, forcetablecreation):
        exists_tables = file_exists(PersistencyDDL.usertable_path);
        try:
            self.setuptables(forcetablecreation, exists_tables);
        except Exception as e:
            logging.error(e)
            raise e

    @classmethod
    def createtable(self, filePointer, statement):
        try:
            c = self.pre_statement(filePointer)
            c.execute(statement)
            self.post_statement()
        except Exception as e:
            logging.error(e)
            raise e

    @classmethod
    def erasedatabase(self):

        os.remove(PersistencyDDL.usertable_path)
        if file_exists(PersistencyDDL.specialtytable_path): os.remove(PersistencyDDL.specialtytable_path)
        if file_exists(PersistencyDDL.doctortable_path): os.remove(PersistencyDDL.doctortable_path)

    @classmethod
    def pre_statement(self, filePointer):
        self.conn = sqlite3.connect(filePointer)
        return self.conn.cursor()

    @classmethod
    def post_statement(self):
        self.conn.commit()
        self.conn.close()

    @classmethod
    def setuptables(self, forcetablecreation, exists_tables):

        if forcetablecreation:
            if exists_tables:
                self.erasedatabase()
            self.createtable(PersistencyDDL.usertable_path, PersistencyDDL.create_user)
            self.createtable(PersistencyDDL.specialtytable_path, PersistencyDDL.create_specialty)
            self.createtable(PersistencyDDL.doctortable_path, PersistencyDDL.create_doctor)


