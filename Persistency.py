# DDL and main database "singleton" connection
import logging
import sqlite3

import PersistencyDDL


class Persistency:
    conn = 0

    def __init__(self, forcetablecreation):
        if forcetablecreation:
            self.createTable(PersistencyDDL.create_user)
            self.createTable(PersistencyDDL.create_specialty)
            self.createTable(PersistencyDDL.create_doctor)
            self.setuptables();

    @classmethod
    def createTable(self, filePointer, statement):
        try:
            c = self.pre_statement(filePointer)
            c.execute(statement)
            self.post_statement(self)
        except Exception as e:
            logging.error(e)
            raise(e)

    @classmethod
    def pre_statement(self, filePointer):
        self.conn = sqlite3.connect(filePointer)
        return self.conn.cursor()

    @classmethod
    def post_statement(self):
        self.conn.commit()
        self.conn.close()

    @classmethod
    def setuptables(self, filepointer):
        pass

