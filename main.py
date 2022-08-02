# ------------------------------------------------------------------------------------------------------------------- #
# Conestoga College, Waterloo. Course: Big data Solutions Architecture                                                #
# THIS SOLUTION WAS CREATED AND DEVELOPED TO THE FINAL PROJECT OF PROG 8420 - PROGRAMMING FOR BIG DATA                #
# Professor: Marcos Bittercourt                                                                                       #
# Team: 8846594 – Sergio Franco de Sa                                                                                 #
#       8807728 – Letícia de Moura                                                                                    #
#       8809338 - Rener Garcia                                                                                        #
#       8738402 - Jennifer Nelson                                                                                     #
# README FIRST: The database creation is being performed by the setup method which is called in the line 124 of this  #
#               file. In order to create it properly it is necessary to uncomment the line 124, and after this make   #
#               sure to comment it back again. This, not only create the database but also insert a minimum amount    #
#               of data.                                                                                              #
# ------------------------------------------------------------------------------------------------------------------- #
import logging

from User import User
from Doctor import Doctor

from ViewControl.Menu import Menu
from ViewControl.SessionManager import SessionManager
from Persistency import Persistency

# Initiating dependent classes
per = Persistency()
session = SessionManager(per)


def setup():
    # Drop all tables
    per.setup_tables(0)

    # Create all tables
    per.setup_tables(1)
    per.setup_data()


def menu_admin(logged_user):
    while True:
        opt = Menu.authorize(logged_user)
        if opt == '1.1':
            Menu.appointment()
        elif opt == '1.2':
            Menu.updateAppointment()
        elif opt == '1.3':
            Menu.findAppointmentDoctor()
        elif opt == '1.4':
            Menu.findAppointmentPatient()
        elif opt == '2.1':
            doc_name = Menu.get_doctor()
            new_user = User(doc_name, None, None, None)
            find_doc = Doctor(new_user, None, None, None, None)
            new_doctor = find_doc.findDoctor()
            logging.info('Doctor found! Collecting the actions from the client!')
            doc_opt = Menu.doctor_option(new_doctor)
        elif opt == '2.2':
            new_doctor = Menu.get_new_doctor()
            new_doctor.save_new_doctor()
            new_doctor.generateAndSaveCalendar()
            logging.info('\n ---The new doctor ' + new_doctor.user.name + ' Successfully created! ---\n')
            print('\n --- The new doctor ' + new_doctor.user.login + ' Successfully created! ---')
        elif opt == '3.1':
            Menu.find_patient()
        elif opt == '3.2':
            Menu.get_new_patient()
        elif opt == '3.3':
            Menu.find_prescriptions()
        elif opt == '4':
            pass
        elif opt == '5':
            print("Good bye! Thank you for using our Walk-in Clinic Software.")
            break
        else:
            print("Invalid option selected")


def menu_doctor(logged_user):
    while True:
        opt = Menu.authorize(logged_user)
        if opt == '1':
            Menu.find_patient()
        elif opt == '2':
            Menu.findAppointmentDoctor(logged_user.login)
        elif opt == '3':
            Menu.prescription(logged_user.login, logged_user.id)
        elif opt == '4':
            Menu.find_prescriptionsByDoctor(logged_user.login,  logged_user.id, logged_user.name)
        elif opt == '5':
            break
        else:
            print("Invalid option selected")


def menu_analyst(logged_user):
    while True:
        opt = Menu.authorize(logged_user)
        if opt == '1.1':
            Menu.appointment()
        elif opt == '1.2':
            Menu.updateAppointment()
        elif opt == '1.3':
            Menu.findAppointmentDoctor()
        elif opt == '1.4':
            Menu.findAppointmentPatient()
        elif opt == '2.1':
            Menu.find_patient()
        elif opt == '2.2':
            Menu.get_new_patient()
        elif opt == '3':
            print("Good bye! Thank you for using our Walk-in Clinic Software.")
            break
        else:
            print("Invalid option selected")


def login():
    #setup()
    try:
        auth_info = Menu.menu_auth()
        if session.auth_user(auth_info[0], auth_info[1]):
            if session.logged_user.role == "ADMIN":
                menu_admin(session.logged_user)
            elif session.logged_user.role == "DOCTOR":
                menu_doctor(session.logged_user)
            elif session.logged_user.role == "ANALYST":
                menu_analyst(session.logged_user)
    except Exception as e:
        logging.error("Login Error: USER OR PASSWORD NOT FOUND! Try again...")
    except IndexError as e:
        logging.error("Data input format is invalid")


if __name__ == '__main__':
    login()
