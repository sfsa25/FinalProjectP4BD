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
        self.id_doc = None

    def pre_statement(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn.cursor()

    def post_statement(self):
        self.conn.commit()
        self.conn.close()

    def execute_command_transaction(self, statement, transaction=False):
        try:
            c = self.conn.cursor()
            c.execute(statement)

        except Exception as e:
            logging.error(e)
            raise e

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
                last_id = c.lastrowid
            self.post_statement()
            return last_id
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
            PersistencyDML.insert_user + "'" + doctor.user.name + "', '" + doctor.user.login + "','" + doctor.user.passwd + "', '" + doctor.user.role + "')",
            PersistencyDML.insert_doctor + "(SELECT MAX(ID) FROM USER), " + doctor.specialty + ",\"" + str(
                doctor.workingdays) + "\", \"" + doctor.shifts + "\" )"]

        return self.execute_transaction(statements)

    def researchDoctor(self, doctor):
        try:
            self.findUserByName(doctor.user)
            result_doctor = self.execute_select(
                PersistencyDML.select_all_doctor + " WHERE USERID = " + str(doctor.user.id))
            doctor.specialty = result_doctor[0][2]
            doctor.workingdays = result_doctor[0][4]
            doctor.shifts = result_doctor[0][3]
        except LookupError as e:
            raise e

        return doctor

    def allDoctors(self):
        return self.execute_select(PersistencyDML.select_doctor_id)

    def findDoctorByLogin(self, login):
        return self.execute_select_pandas(PersistencyDML.select_doctor_id + f"  WHERE U.LOGIN LIKE '{login}'")

    def findUserByName(self, user):
        result_user = self.execute_select(PersistencyDML.select_all_user + " WHERE NAME = '" + user.name + "'")
        if result_user and len(result_user):
            user.id = result_user[0][0]
            user.login = result_user[0][1]
            user.role = result_user[0][2]
        else:
            raise LookupError("USER NOT FOUND!")

        return user

    def findDoctorByName(self, name):
        query = PersistencyDML.select_doctor_id + f" WHERE U.NAME LIKE '{name}'"
        return self.execute_select_pandas(query)

    def findDoctorByID(self, doctor_id):
        query = PersistencyDML.select_doctor_id + f" WHERE d.ID = {doctor_id}"
        return self.execute_select_pandas(query)

    # Time Slots

    def insertTimeTable(self, timetable, doc_id):
        listofqueries = []

        for time in timetable:
            query = PersistencyDML.insert_calendar + str(doc_id) + ", '" + str(time) + "', \"" + str(
                timetable[time][0]) + "\")"
            listofqueries.append(query)

        result_user = self.execute_transaction(listofqueries)

    def findDoctorTimeTable(self, doctor_id):
        query = PersistencyDML.select_all_timetable + " WHERE DOCTOR_ID = " + doctor_id
        result_doctor = self.execute_select(query)

    def findDateSlots(self, dat, doctor_id):
        query = PersistencyDML.select_all_timetable + \
                f" WHERE doctor_id = {doctor_id} AND strftime('%d-%m-%Y', DATE_STAMP) = '{dat}'"
        return self.execute_select(query)

    def updateSlot(self, dat, slot, doctor_id):
        query = PersistencyDML.updateTimeSlot + "\"" + str(
            slot) + """\" WHERE strftime("%d-%m-%Y", DATE_STAMP) = '""" + str(dat) + "'" \
                + f" AND doctor_id = {doctor_id}"

        return self.execute_command(query)

    def findFreeDateByDoctor(self, doctor):
        query = f"SELECT strftime('%d-%m-%Y', DATE_STAMP) DATES, TIMESLOT FROM TIMETABLE " \
                f"WHERE DOCTOR_ID = {doctor}  AND DATE_STAMP BETWEEN DATE(CURRENT_DATE, '-1 days') " \
                f"AND DATE(CURRENT_DATE, '+60 days')"
        return self.execute_select(query)

    # Prescription

    def insertPrescribe(self, patient_id, doctor_id, medication, observation):
        query = f"INSERT INTO PRESCRIPTION (patient_id,doctor_id,medication,observation) VALUES ({patient_id},{doctor_id},'{medication}','{observation}')"

        return self.execute_command(query)

    def findPrescriptionbyDoctor(self, doctor_id, patient_id):

        query = f"SELECT medication, observation, date_created FROM PRESCRIPTION " \
                f"WHERE doctor_id = {doctor_id} AND patient_id = {patient_id}"

        return self.execute_select(query)

    # Appointment

    def insertAppointment(self, patient_id, doctor_id, appointment_date, slot, new_slot):
        statements = [f"INSERT INTO APPOINTMENT (patient_id,doctor_id,appointment_date,slot) "
                      f"VALUES ({patient_id},{doctor_id},'{appointment_date}','{slot}')",
                      PersistencyDML.updateTimeSlot + "\"" + str(
                          new_slot) + """\" WHERE strftime("%d-%m-%Y", DATE_STAMP) = '""" + str(appointment_date) + "'"
                      + f" AND doctor_id = {doctor_id}"]

        return self.execute_transaction(statements)

    def updateAppointment(self, appointment_id, doctor_id, appointment_date, slot, removed_slot, prior_date, returned_slot):
        statements = [f"UPDATE APPOINTMENT SET doctor_id = {doctor_id}, " +
                      f"appointment_date = '{appointment_date}', slot = '{slot}' WHERE ID = {appointment_id}",
                      PersistencyDML.updateTimeSlot + "\"" + str(
                          returned_slot) + """\" WHERE strftime("%d-%m-%Y", DATE_STAMP) = '""" + str(prior_date) + "'"
                      + f" AND doctor_id = {doctor_id}",
                      PersistencyDML.updateTimeSlot + "\"" + str(
                          removed_slot) + """\" WHERE strftime("%d-%m-%Y", DATE_STAMP) = '""" + str(appointment_date) + "'"
                      + f" AND doctor_id = {doctor_id}"
                      ]

        return self.execute_transaction(statements)

    def findAppointmentByDoctor(self, doctor):
        query = f"SELECT p.first_name, p.last_name, a.appointment_date, a. slot, a.doctor_id " \
                f"FROM APPOINTMENT a INNER JOIN PATIENT p ON  a.patient_id = p.ID " \
                f"WHERE doctor_id = {doctor}"

        return self.execute_select(query)

    def findAppointmentByPatient(self, patient):
        query = f"SELECT p.first_name, p.last_name, a.appointment_date, a.slot, a.doctor_id, a.ID " \
                f"FROM APPOINTMENT a INNER JOIN PATIENT p ON a.patient_id = p.ID " \
                f"WHERE patient_id = {patient}"

        return self.execute_select(query)
