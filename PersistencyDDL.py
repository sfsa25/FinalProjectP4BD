# DDL of the database

create_user = """CREATE TABLE IF NOT EXISTS USER(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    LOGIN TEXT UNIQUE NOT NULL ,
                    USERTYPE TEXT NOT NULL,
                    USERTYPE TEXT NOT NULL,
               CRYPTOGRAPHIC_PASSWD TEXT NOT NULL
               )"""

create_specialty = """CREATE TABLE IF NOT EXISTS SPECIALTY(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            SPECIALTY TEXT NOT NULL )"""

create_doctor = """CREATE TABLE IF NOT EXISTS DOCTOR(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           USERID INTEGER NOT NULL,
                           DOCTOR_TYPE INTEGER NOT NULL,
                           SHIFTS TEXT,
                           WORKING_DAYS TEXT NOT NULL,
                     FOREIGN KEY(DOCTOR_TYPE) REFERENCES SPECIALTY(ID),
                     FOREIGN KEY(USERID) REFERENCES USER(ID))"""

create_patient = """CREATE TABLE IF NOT EXISTS PATIENT(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           FIST_NAME TEXT NOT NULL,
                           LAST_NAME TEXT NOT NULL,
                           GENDER CHAR NOT NULL,
                           DOB DATE NOT NULL,
                           EMAIL TEXT NOT NULL,
                           DATA_CREATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                           """

create_appointment = """CREATE TABLE IF NOT EXISTS APPOINTMENT(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           PATIENT_ID INTEGER NOT NULL,
                           DOCTOR_ID INTEGER NOT NULL, 
                           START_TIME DATETIME NOT NULL,
                           END_TIME DATETIME NOT NULL,
                           FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(ID),
                           FOREIGN KEY(DOCTOR_ID) REFERENCES DOCTOR(ID))
                           """

create_prescription = """CREATE TABLE IF NOT EXISTS PRESCRIPTION(
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           APPOINTMENT_ID INTEGER NOT NULL,
                           DATE_CREATED DATETIME NOT NULL,
                           MEDICATION TEXT
                           DOSE TEXT,
                           OBSERVATION TEXT,
                           FOREIGN KEY(APPOINTMENT_ID) REFERENCES APPOINTMENT(ID))
                           """

create_timetable = """CREATE TABLE IF NOT EXISTS TIMETABLE (
                           ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           DOCTOR_ID INTEGER NOT NULL,
                           DATE_STAMP TIMESTAMP NOT NULL,
                           TIMESLOT TEXT,
                           FOREIGN KEY(DOCTOR_ID) REFERENCES DOCTOR(ID))
                           """

drop_user = """DROP TABLE IF EXISTS USER"""
drop_doctor = """DROP TABLE IF EXISTS DOCTOR"""
drop_prescription = """DROP TABLE IF EXISTS PRESCRIPTION"""
drop_specialty = """DROP TABLE IF EXISTS SPECIALTY"""
drop_appointment = """DROP TABLE IF EXISTS PRESCRIPTION"""
drop_patient = """DROP TABLE IF EXISTS PATIENT"""
drop_timetable = """DROP TABLE IF EXISTS TIMETABLE"""

list_create_table = [create_user, create_specialty, create_doctor, create_patient, create_appointment, create_prescription, create_timetable]
list_drop_table = [drop_doctor, drop_patient, drop_user, drop_specialty, drop_appointment, drop_prescription, drop_timetable]
db_path = "Database/walkclinic_.db"


