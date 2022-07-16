#DDL of the database
create_user = ("CREATE TABLE IF NOT EXISTS USER( \n"
               "            ID INTEGER PRIMARY KEY AUTOINCREMENT, \n"
               "            LOGIN TEXT not null, \n"
               "            USERTYPE ENUM('ADMIN','ANALYST','DOCTOR') NOT NULL,\n"
               "            CRYPTOGRAPHIC_PASSWD TEXT not null)")

create_specialty = ("CREATE TABLE IF NOT EXISTS SPECIALTY( \n"
               "            ID INTEGER PRIMARY KEY AUTOINCREMENT, \n"
               "            SPECIALTY ENUM['ADMIN', 'DOCTOR', 'ANALYST'] NOT NULL")

create_doctor = ("CREATE TABLE IF NOT EXISTS DOCTOR( \n"
               "            ID INTEGER PRIMARY KEY AUTOINCREMENT, \n"
               "            LOGIN TEXT not null, \n"
               "            USERTYPE INTEGER NOT NULL,\n"
               "            USERID INTEGER NOT NULL,\n"
               "            CRYPTOGRAPHIC_PASSWD TEXT not null) "
                     "FOREIGN KEY(USERTYPE) REFERENCES SPECIALTY(ID),"
                     "FOREIGN KEY(USERID) REFERENCES USER(ID)")