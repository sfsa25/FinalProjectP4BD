#DDL of the database
create_user = """CREATE TABLE IF NOT EXISTS USER(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\n
                    LOGIN TEXT NOT NULL ,
                    USERTYPE TEXT NOT NULL,
               CRYPTOGRAPHIC_PASSWD TEXT NOT NULL
               )"""

create_specialty = """CREATE TABLE IF NOT EXISTS SPECIALTY(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            SPECIALTY TEXT NOT NULL )"""

create_doctor = """CREATE TABLE IF NOT EXISTS DOCTOR(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           LOGIN TEXT not null,
                           USERTYPE INTEGER NOT NULL,
                           USERID INTEGER NOT NULL,
                           CRYPTOGRAPHIC_PASSWD TEXT not null,
                     FOREIGN KEY(USERTYPE) REFERENCES SPECIALTY(ID),
                     FOREIGN KEY(USERID) REFERENCES USER(ID))"""

usertable_path = "C:/Users/sergi/PycharmProjects/FinalProjectP4BD/Database/user.db"
specialtytable_path = "C:/Users/sergi/PycharmProjects/FinalProjectP4BD/Database/specialty.db"
doctortable_path = "C:/Users/sergi/PycharmProjects/FinalProjectP4BD/Database/doctor.db"