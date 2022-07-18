import logging
from typing import re

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
            print(" -- 3.1 - Find (or change) an appointment")
            print(" -- 3.2 - Register a new patient")
            print("4 - Reports")
        elif user.role == "DOCTOR":
            print("---Welcome doctor " + user.login+" ---")
            print("Doctors Menu:\n")
            print("1 - Find a doctor \n")
            print("2 - Register a new doctor\n")
            print("1 - Create a schedule\n")
        elif user.role == "ANALYST":
            print("---Welcome analyst " + user.login+" ---")

        return input("Please type your chosen option here: \n")

    @staticmethod
    def get_new_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        user_login = input("PLEASE, TYPE YOUR LOGIN: ")
        user_passwd = input("PLEASE, TYPE YOUR PASSWORD:")
        doc_specialty = input("PLEASE, CHOOSE A SPECIALTY ( 1 - Cardiologist, 2 - Physician, 3 - Family Care):")
        user = User(user_login, 'DOCTOR', user_passwd)
        doc = Doctor(user, doc_specialty)
        logging.info("New Doctor instance created: doc.user.login: "+doc.user.login);
        return doc;

    @staticmethod
    def get_doctor():
        print("--->REGISTER A NEW DOCTOR<---")
        return input("PLEASE, TYPE THE DOCTOR'S LOGIN: ")

    @staticmethod
    def doctor_option(doc_login):
        print('Doctor '+ doc_login + ' found!')
        print('What would you like to do?:')
        return input('0 - Exit, 1 - Create a schedule, 2 - Find an appointment')

