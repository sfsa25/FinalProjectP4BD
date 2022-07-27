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
        try:
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
                # NO INPUTS HERE, PLEASE... HEAD TO MENU
                new_doctor = Menu.get_new_doctor()
                new_doctor.save_new_doctor()
                new_doctor.generateAndSaveCalendar()
                logging.info('\n ---The new doctor ' + new_doctor.user.name + ' Successfully created! ---\n')
                print('\n --- The new doctor ' + new_doctor.user.login + ' Successfully created! ---')
            elif opt == '2.3':
                pass
            elif opt == '3.1':
                pass
            elif opt == '3.2':
                pass
            elif opt == '3.3':
                Menu.find_prescriptions()
            elif opt == '4':
                pass
            elif opt == '5':
                break
            #else:
                #raise IndexError(DOCTOR No)
        except LookupError as e:
            print("Doctor Not Found! Please try again.\n\n")
            #raise e
        except IndexError as ie:
            print("Information has Invalid format\n\n")
            #raise ie


def menu_doctor(logged_user):
    while True:
        opt = Menu.authorize(logged_user)

        if opt == '1':
            print('Find a patient')
            # findpatient

        elif opt == '2':
            Menu.findAppointmentDoctor(logged_user.login)
        elif opt == '3':
            Menu.prescription(logged_user.login)
        elif opt == '4':
            Menu.find_prescriptionsByDoctor(logged_user.login)
        elif opt == '5':
            break
        else:
            raise IndexError("Invalid option selected")


def login():
    # setup()
    try:
        auth_info = Menu.menu_auth()
        if session.auth_user(auth_info[0], auth_info[1]):
            if session.logged_user.role == "ADMIN":
                menu_admin(session.logged_user)
            elif session.logged_user.role == "DOCTOR":
                menu_doctor(session.logged_user)
    except Exception as e:
        logging.error("Login Error: USER OR PASSWORD NOT FOUND! Try again...")
    except IndexError as e:
        logging.error("Data input format is invalid")


if __name__ == '__main__':
    login()
