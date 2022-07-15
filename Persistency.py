#DDL and main database "singleton" connection

import sqlite3

class Persistency:
    conn = 0

    @classmethod
    def createTable(self, filePointer, statement):
        try:
            c = self.pre_statement(filePointer)
            c.execute(statement)

            self.post_statement(self)
        except Exception as e:
            print(e)

    @classmethod
    def pre_statement(self, filePointer):
        self.conn = sqlite3.connect(filePointer)
        return self.conn.cursor()

    @classmethod
    def post_statement(self):
        self.conn.commit()
        self.conn.close()