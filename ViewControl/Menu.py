import logging

import StaticPatterns
import EntryValidation
import re
from Doctor import Doctor
from User import User
from Prescription import Prescription
from Patient import Patient
from Appointment import Appointment
from ViewControl.EntryValidation import EntryValidation


class Menu:

    @staticmethod
    def menu_auth():
        login = input("Enter your login: \n")
        if EntryValidation.validateField(login, StaticPatterns.LOGIN_PATTERN):
            passwd = input("Enter your password: ")
            if not EntryValidation.validateField(passwd, StaticPatterns.PASSWD_PATTERN):
                logging.ERROR("Invalid password format. Format accepted: 4 digits")
                raise IndexError("Password format is invalid")
        else:
            logging.ERROR("Invalid login format. Format accepted: 4 to 25 string length")
            raise IndexError("Login format is invalid")

        return [login, passwd]

    @staticmethod
    def authorize(user):
        if user.role == "ADMIN":
            print("---Welcome admin " + user.name + ", login: " + user.login)
            print("Appointment Menu")
            print(" -- 1.1 - Book an appointment ")
            print(" -- 1.2 - Update an appointment")
            print(" -- 1.3 - Find an appointment by Doctor")
            print(" -- 1.4 - Find an appointment by Patient")
            print("Doctors Menu:")
            print(" -- 2.1 - Find a doctor ")
            print(" -- 2.2 - Register a new doctor")
            print(" -- 2.3 - Create a schedule")
            print("Patients Menu:")
            print(" -- 3.1 - Find a patient")
            print(" -- 3.2 - Register a new patient")
            print(" -- 3.3 - Find a prescription")
            print("4 - Reports")
            print("5 - Exit")
        elif user.role == "DOCTOR":
            print("---Welcome doctor " + user.name + ", login: " + user.login)
            print("Doctors Menu:")
            print("1 - Find a patient ")
            print("2 - Find an appointment")
            print("3 - Prescribe")
            print("4 - Find a prescription ")
            print("5 - Exit\n")
        elif user.role == "ANALYST":
            print("---Welcome analyst " + user.login + " ---")
            print(" -- 1.1 - Book an appointment ")
            print(" -- 1.2 - Update an appointment")
            print(" -- 1.3 - Find an appointment by Doctor")
        return input("Please type your chosen option here: \n")
    @staticmethod
    def get_new_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        userName = input("PLEASE, TYPE THE DOCTOR'S NAME: ")
        userLogin = input("PLEASE, TYPE THE DOCTOR'S LOGIN: ")
        userPasswd = input("PLEASE, TYPE THE DOCTOR'S PASSWORD:")
        docSpecialty = input("PLEASE, CHOOSE A SPECIALTY ( 1 - Cardiologist, 2 - Physician, 3 - Family Care):")
        docWorkingDays = input("""PLEASE, TYPE WORKING DAYS(Pattern: ['Monday','Tuesday', 'Wednesday']): """)
        docshifts = input(
            """PLEASE, TYPE SHIFT(Pattern : ['1', '2', '3'], 1 - Morning, 2 - Afternoon, 3 - Evening): """)
        user = User(userName, userLogin, 'DOCTOR', userPasswd)
        doc = Doctor(user, docSpecialty, docWorkingDays, docshifts, None)
        logging.info("New Doctor instance created: doc.user.login: " + doc.user.login);
        return doc

    @staticmethod
    def get_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        return input("PLEASE, TYPE THE DOCTOR'S NAME: ")

    @staticmethod
    def doctor_option(doc: Doctor):
        print('Doctor ' + doc.user.login + ' found! This is (are) his working day(s):' + doc.workingdays)
        print('What would you like to do?:')
        return input('0 - Exit, 2 - Create an appointment for this doctor')

    @staticmethod
    def prescription(login):
        name = input("Patient Name: ")
        patient = Patient().findPatient(name)
        if not patient.empty:
            while True:
                medication = input("Medication: ")
                observation = input("Observations: ")
                doctor = Doctor().findDoctorID(login)
                prescribe = Prescription(patient['ID'][0], doctor['ID'][0], medication, observation)
                prescribe.insertPrescription()
                opt = input('Do you want to add another medication? Y-YES X-EXIT \n')
                if not opt == 'Y':
                    break
        else:
            print('Patient not found.\n')

    @staticmethod
    def find_prescriptionsByDoctor(login):
        name = input("Patient Name: ")
        patient = Patient().findPatient(name)
        if not patient.empty:
            doctor = Doctor().findDoctorLogin(login)
            prescribe = Prescription(patient['ID'][0], doctor['ID'][0])
            doctor_name = doctor['NAME'][0]
            list_medication = prescribe.findPrescription()
            if len(list_medication) > 0:
                print(f'--- Patient: {name}')
                print(f'--- Prescriptions made by {doctor_name}  --- \n')
                for med, obs, date in list_medication:
                    print(f'Date Created: {date} - Medication: {med} - Observation {obs}')
                print()
            else:
                print('There are no prescriptions for this patient.')
        else:
            print('Patient not found.\n')

    @staticmethod
    def find_prescriptions():
        name = input("Patient Name: ")
        patient = Patient().findPatient(name)
        if not patient.empty:
            doctors = Doctor().getallDoctors()
            if len(doctors) > 0:
                for id, doctor_name in doctors:
                    prescribe = Prescription(patient['ID'][0], id)
                    list_medication = prescribe.findPrescription()
                    if len(list_medication) > 0:
                        print(f'--- Patient: {name}')
                        print(f'--- Prescriptions made by {doctor_name}  --- \n')
                        for med, obs, date in list_medication:
                            print(f'Date Created: {date} - Medication: {med} - Observation {obs}')
                        print()
                    else:
                        print('There are no prescriptions for this patient.')
            else:
                print('There are no registered doctors.')
        else:
            print('Patient not found.\n')

    # Appointment

    @staticmethod
    def findAppointmentDoctor(login=None):
        doctor = None
        if login is None:
            doctor_name = input("Doctor Name: ")
            doctor = Doctor().findDoctorName(doctor_name)
        else:
            doctor = Doctor().findDoctorLogin(login)

        if not doctor.empty:
            doctor_name = doctor['NAME'][0]
            doctor_id = doctor['ID'][0]
            appointments = Appointment().findAppointmentDoctor(doctor_id)
            if len(appointments) > 0:
                print(f'--- Appointments Doctor {doctor_name}')
                for app in appointments:
                    print(f'Patient: {app[0]}  {app[1]}')
                    print(f'Date: {app[2]} - Time: {app[3]} ')
            else:
                print('No appointments were found.')
        else:
            print('Doctor not found.\n')

        input("Press Enter to go back to Menu.")

    @staticmethod
    def findAppointmentPatient():
        patient_name = input("Patient Name: ")
        patient = Patient().findPatient(patient_name)
        if not patient.empty:
            patient_id = patient['ID'][0]
            appointments = Appointment().findAppointmentPatient(patient_id)
            if len(appointments) > 0:
                print(f'Patient: {patient_name}')
                print(f'--- Appointments')
                for app in appointments:
                    doctor = Doctor().findDoctorId(app[4])
                    doctor_name = doctor['NAME'][0]
                    print(f'Date: {app[2]} - Time: {app[3]} with Doctor {doctor_name}')
            else:
                print('No appointments were found.')
        else:
            print('Patient not found.\n')

        input("Press Enter to go back to Menu.")

    @staticmethod
    def chooseDateSlot(times):
        print('Available dates:')
        for i, time in enumerate(times):
            print(f'{i} - {time[0]}')

        option = EntryValidation.choose_option(len(times),
                                               "Choose the date indicated by the number in front: ")
        chosen_date = times[option][0]

        print(f'Slot times available for {chosen_date} :')
        slots = re.findall(StaticPatterns.slots, times[option][1])
        for i, slot in enumerate(slots):
            print(f'{i} - {slot}')

        option = EntryValidation.choose_option(len(slots),
                                               "Choose the slot indicated by the number in front: ")
        chosen_slot = slots[option]

        return [chosen_date, chosen_slot]

    @staticmethod
    def updateAppointment():
        doctor = Doctor()

        patient_name = input("Patient Name: ")
        patient = Patient().findPatient(patient_name)
        if not patient.empty:
            patient_id = patient['ID'][0]
            appointments = Appointment().findAppointmentPatient(patient_id)
            if len(appointments) > 0:
                print(f'Patient: {patient_name}')
                print(f'--- Appointments')

                for i, app in enumerate(appointments):
                    result = doctor.findDoctorId(app[4])
                    doctor_name = result['NAME'][0]
                    print(f'{i} - Date: {app[2]} - Time: {app[3]} with Doctor {doctor_name}')

                option = EntryValidation.choose_option(len(appointments),
                                                       "Choose the appointment to be changed: ")
                chose_app = appointments[option]

                same_doctor = EntryValidation.choose_option(2,
                                                            "\nDo you want to reschedule with the same doctor? 1-Yes 2-No")

                result = None
                if same_doctor == 2:
                    doctor_name = input("Doctor Name: ")
                    result = doctor.findDoctorName(doctor_name)

                    while result.empty:
                        print('Doctor not found. Choose again.\n')
                        doctor_name = input("Doctor Name: ")
                        result = doctor.findDoctorName(doctor_name)
                else:
                    result = doctor.findDoctorId(chose_app[4])

                doctor_id = result['ID'][0]
                doctor_name = result['NAME'][0]

                times = doctor.findFreeDate(doctor_id)
                if len(times) > 0:
                    chosen_date, chosen_slot = Menu.chooseDateSlot(times)
                    prior_date = chose_app[2]
                    appointment_id = chose_app[5]

                    removed_slot = doctor.removeSlot(chosen_date, chosen_slot, doctor_id)
                    returned_slot = doctor.returnSlot(prior_date, chose_app[3], doctor_id)

                    appointment = Appointment(patient_id, doctor_id, chosen_date, chosen_slot, appointment_id)
                    appointment.update(removed_slot, prior_date, returned_slot)

                    print(f'\nAppointment rescheduled for {patient_name} on the day {chosen_date} '
                          f'with Doctor {doctor_name} between {chosen_slot}\n')

                else:
                    print('No dates available\n')
            else:
                print('No appointments were found.\n')

        else:
            print('Patient not found.\n')

        input("Press Enter to go back to Menu.")

    @staticmethod
    def appointment():
        doctor = Doctor()
        patient_name = input("Patient Name: ")
        patient = Patient().findPatient(patient_name)
        if not patient.empty:
            patient_id = patient['ID'][0]
            doctor_name = input("Doctor Name: ")
            result = doctor.findDoctorName(doctor_name)
            if not result.empty:
                doctor_id = result['ID'][0]
                times = doctor.findFreeDate(doctor_id)
                if len(times) > 0:

                    chosen_date, chosen_slot = Menu.chooseDateSlot(times)

                    new_slot = doctor.removeSlot(chosen_date, chosen_slot, doctor_id)
                    appointment = Appointment(patient_id, doctor_id, chosen_date, chosen_slot)
                    appointment.insert(new_slot)

                    print(f'\nAppointment scheduled for {patient_name} on the day {chosen_date} '
                          f'with Doctor {doctor_name} between {chosen_slot}\n')
                else:
                    print('No dates available\n')
            else:
                print('Doctor not found.\n')
        else:
            print('Patient not found.\n')

        input("Press Enter to go back to Menu.")

    @staticmethod
    def get_new_patient():
        print("--->REGISTER A NEW PATIENT<---")
        patient_first_name = input("PLEASE, TYPE THE PATIENT'S FIRST NAME: ")
        patient_last_name = input("PLEASE, TYPE THE PATIENT'S LAST NAME: ")
        patient_gender = input("PLEASE, TYPE THE PATIENT'S GENDER: (Type F for Female or type M for Male) ")
        patient_dob = input("PLEASE, TYPE THE PATIENT'S DATE OF BIRTH: (YYYY-MM-DD Format) ")
        patient_email = input("PLEASE, TYPE THE PATIENT'S E-MAIL: ")
        patient = Patient(patient_first_name, patient_last_name, patient_gender, patient_dob, patient_email)
        patient.insert()
        print('Patient successfully inserted!\n')

    @staticmethod
    def find_patient():
        print("--->FIND A PATIENT<---")
        patient_first_name = input("PLEASE, TYPE THE PATIENT'S FIRST NAME: ")
        patient_last_name = input("PLEASE, TYPE THE PATIENT'S LAST NAME: ")
        patientReturned = Patient().findPatientByFullName(patient_first_name, patient_last_name)

        if len(patientReturned) > 0:
            for i in patientReturned:
                # Pat.patient_email = l[0]
                patientId = i[0]
                firstName = i[1]
                lastName = i[2]

            print(f'Patient ID: {patientId}, {firstName} {lastName} found in Database.\n')
        else:
            print('Patient not found!\n')
