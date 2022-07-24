# DML

select_all_user = """SELECT * FROM USER"""
select_all_doctor = """SELECT * FROM DOCTOR"""
select_all_specialty = """SELECT * FROM SPECIALTY"""
select_all_appointment = """SELECT * FROM APPOINTMENT"""
select_all_prescription = """SELECT * FROM PRESCRIPTION"""
select_all_patient = """SELECT * FROM PATIENT"""
select_all_timetable = """SELECT * FROM TIMETABLE"""


initial_users = """INSERT INTO USER (NAME, LOGIN,USERTYPE,CRYPTOGRAPHIC_PASSWD) VALUES ('ADMIN_NAME','SUPERADMIN', 'ADMIN', '1234')"""
initial_specialties = """INSERT INTO SPECIALTY (SPECIALTY) values ('Cardiologist'), ('Physician'), ('Family Care')"""
initial_doctor = """INSERT INTO DOCTOR (USERID, DOCTOR_TYPE, WORKING_DAYS, SHIFTS) VALUES ('1', '1', "['Monday', 'Friday']", "['1', '2']")"""

insert_calendar = """INSERT INTO TIMETABLE (DOCTOR_ID, DATE_STAMP, TIMESLOT) VALUES ("""
insert_user = """INSERT INTO USER (NAME, LOGIN,CRYPTOGRAPHIC_PASSWD, USERTYPE) VALUES ("""
insert_doctor = """INSERT INTO DOCTOR (USERID, DOCTOR_TYPE, WORKING_DAYS, SHIFTS) VALUES ("""

list_initial_data = [initial_users, initial_specialties, initial_doctor]
updateTimeSlot  = "UPDATE TIMETABLE SET TIMESLOT = "
begin_transaction = "BEGIN TRANSACTION"