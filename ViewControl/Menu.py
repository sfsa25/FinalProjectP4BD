import logging

import StaticPatterns
from Doctor import Doctor
from User import User
from ViewControl.EntryValidation import EntryValidation
import Menu


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
            print("---Welcome admin " + user.login+" ---")
            print("1 - Book an appointment")
            print("Doctors Menu:")
            print(" -- 2.1 - Find a doctor ")
            print(" -- 2.2 - Register a new doctor")
            print(" -- 2.3 - Create a schedule")
            print("Patients Menu:")
            print(" -- 3.1 - Find an appointment")
            print(" -- 3.2 - Register a new patient")
            print("4 - Reports")
            print("5 - Exit")
        elif user.role == "DOCTOR":
            print("---Welcome doctor " + user.login+" ---")
            print("Doctors Menu:\n")
            print("1 - Find a patient \n")
            print("2 - Find an appointment\n")
            print("3 - Prescribe\n")
            print("4 - Find prescription\n")
            print("5 - Exit")
        elif user.role == "ANALYST":
            print("---Welcome analyst " + user.login+" ---")

        return input("Please type your chosen option here: \n")

    @staticmethod
    def get_new_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        userLogin = input("PLEASE, TYPE YOUR LOGIN: ")
        userPasswd = input("PLEASE, TYPE YOUR PASSWORD:")
        docSpecialty = input("PLEASE, CHOOSE A SPECIALTY ( 1 - Cardiologist, 2 - Physician, 3 - Family Care):")
        docWorkingDays = input("""PLEASE, TYPE WORKING DAYS(Pattern: ['Monday','Tuesday', 'Wednesday']): """)
        docshifts = input("""PLEASE, TYPE SHIFT(Pattern : ['1', '2', '3'], 1 - Morning, 2 - Afternoon, 3 - Evening): """)
        user = User(userLogin, 'DOCTOR', userPasswd)
        doc = Doctor(user, docSpecialty, docWorkingDays, docshifts, None)
        logging.info("New Doctor instance created: doc.user.login: "+doc.user.login);
        return doc

    @staticmethod
    def get_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        return input("PLEASE, TYPE THE DOCTOR'S LOGIN: ")

    @staticmethod
    def doctor_option(doc:Doctor):
        print('Doctor ' + doc.user.login + ' found! This is (are) his working day(s):' + doc.workingdays)
        print('What would you like to do?:')
        return input('0 - Exit, 2 - Create an appointment for this doctor')

