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
            print("---Welcome admin " + user.name+", login: "+user.login)
            print("1 - Book an appointment")
            print("Doctors Menu:")
            print(" -- 2.1 - Find a doctor ")
            print(" -- 2.2 - Register a new doctor")
            print(" -- 2.3 - Create a schedule")
            print("Patients Menu:")
            print(" -- 3.1 - Find an appointment")
            print(" -- 3.2 - Find a patient")
            print(" -- 3.3 - Register a new patient")
            print(" -- 3.4 - Find a prescription")
            print("4 - Reports")
            print("5 - Exit")
        elif user.role == "DOCTOR":
            print("---Welcome doctor " + user.name+", login: "+user.login)
            print("Doctors Menu:")
            print("1 - Find a patient ")
            print("2 - Find an appointment")
            print("3 - Prescribe")
            print("4 - Find a prescription ")
            print("5 - Exit\n")
        elif user.role == "ANALYST":
            print("---Welcome analyst " + user.login+" ---")

        return input("Please type your chosen option here: \n")

    @staticmethod
    def get_new_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        userName =  input("PLEASE, TYPE THE DOCTO'S NAME: ")
        userLogin = input("PLEASE, TYPE THE DOCTOR'S LOGIN: ")
        userPasswd = input("PLEASE, TYPE THE DOCTOR'S PASSWORD:")
        docSpecialty = input("PLEASE, CHOOSE A SPECIALTY ( 1 - Cardiologist, 2 - Physician, 3 - Family Care):")
        docWorkingDays = input("""PLEASE, TYPE WORKING DAYS(Pattern: ['Monday','Tuesday', 'Wednesday']): """)
        docshifts = input("""PLEASE, TYPE SHIFT(Pattern : ['1', '2', '3'], 1 - Morning, 2 - Afternoon, 3 - Evening): """)
        user = User(userName, userLogin, 'DOCTOR', userPasswd)
        doc = Doctor(user, docSpecialty, docWorkingDays, docshifts, None)
        logging.info("New Doctor instance created: doc.user.login: "+doc.user.login);
        return doc

    @staticmethod
    def get_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        return input("PLEASE, TYPE THE DOCTOR'S NAME: ")

    @staticmethod
    def doctor_option(doc:Doctor):
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
                opt= input('Do you want to add another medication? Y-YES X-EXIT \n')
                if not opt == 'Y':
                    break
        else:
            print('Patient not found.\n')

    @staticmethod
    def find_prescriptionsByDoctor(login):
        name = input("Patient Name: ")
        patient = Patient().findPatient(name)
        if not patient.empty:
            doctor = Doctor().findDoctorID(login)
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

    #Appointment

    @staticmethod
    def appointment():
        patient_name = input("Patient Name: ")
        patient = Patient().findPatient(patient_name)
        if not patient.empty:
            patient_id = patient['ID'][0]
            doctor_name = input("Doctor Name: ")
            doctor = Doctor().findDoctorName(doctor_name)
            if not doctor.empty:
                doctor_id = doctor['ID'][0]
                times = Appointment().findFreeDate(doctor_id)
                if len(times) > 0:

                    print('Available dates:')
                    for i, time in enumerate(times):
                        print(f'{i} - {time[0]}')

                    option = EntryValidation.choose_option(len(times),
                                                           "Choose the date indicated by the number in front: ")
                    chosen_date = times[option][0]

                    print(f'Slot times availables for {chosen_date} :')
                    slots = re.findall(StaticPatterns.slots, times[option][1])
                    for i, slot in enumerate(slots):
                        print(f'{i} - {slot}')

                    option = EntryValidation.choose_option(len(slots),
                                                           "Choose the slot indicated by the number in front: ")
                    chosen_slot = slots[option]

                    appointment = Appointment(patient_id, doctor_id,chosen_date,chosen_slot)
                    appointment.insert()

                    Doctor().removeSlot(chosen_date,chosen_slot)

                    print(f'\nAppointment scheduled for {patient_name} on the day {chosen_date} '
                          f'with Doctor {doctor_name} between {chosen_slot}\n')

                else:
                    print('No dates available\n')
            else:
                print('Doctor not found.\n')
        else:
            print('Patient not found.\n')

        input("Press Enter to go back to Menu.")





