# DDL of the database

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

create_patient = """CREATE TABLE IF NOT EXISTS PATIENT(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           FIST_NAME TEXT NOT NULL,
                           LAST_NAME TEXT NOT NULL,
                           GENDER CHAR NOT NULL,
                           DOB DATE NOT NULL,
                           EMAIL TEXT NOT NULL,
                           DATA_CREATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                           """


create_appointment = """CREATE TABLE IF NOT EXISTS APPOINTMENT(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           PATIENT_ID INTEGER NOT NULL,
                           DOCTOR_ID INTEGER NOT NULL, 
                           START_TIME DATETIME NOT NULL,
                           END_TIME DATETIME NOT NULL,
                           FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(ID),
                           FOREIGN KEY(DOCTOR_ID) REFERENCES DOCTOR(ID)
                           """

create_prescription = """CREATE TABLE IF NOT EXISTS PRESCRIPTION(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           APPOINTMENT_ID INTEGER NOT NULL,
                           DATE_CREATED DATETIME NOT NULL,
                           MEDICATION TEXT
                           DOSE TEXT,
                           OBSERVATION TEXT,
                           FOREIGN KEY(APPOINTMENT_ID) REFERENCES APPOINTMENT(ID)
                           """


list_table = [create_user, create_specialty, create_doctor, create_patient, create_appointment, create_prescription]
