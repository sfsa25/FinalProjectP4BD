# DML

select_all_user = """SELECT * FROM USER"""
select_all_doctor = """SELECT * FROM DOCTOR"""
select_all_specialty = """SELECT * FROM SPECIALTY"""
select_all_appointment = """SELECT * FROM APPOINTMENT"""
select_all_prescription = """SELECT * FROM PRESCRIPTION"""
select_all_patient = """SELECT * FROM PATIENT"""


initial_users = """INSERT INTO USER (LOGIN,USERTYPE,CRYPTOGRAPHIC_PASSWD) VALUES ('SUPERADMIN', 'ADMIN', '1234')"""
initial_specialties = """INSERT INTO SPECIALTY (SPECIALTY) values ('Cardiologist'), ('Physician'), ('Family Care')"""

list_initial_data = [initial_users, initial_specialties]