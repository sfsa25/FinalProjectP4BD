import logging

from Doctor import Doctor
from User import User
from Doctor import Doctor
from ViewControl.Menu import  Menu
from ViewControl.SessionManager import SessionManager
from Persistency import Persistency

# Initiating dependent classes
per = Persistency()
session = SessionManager(per)

# Drop all tables
per.setup_tables(0)

# Create all tables
per.setup_tables(1)
per.setup_data()

try:

    auth_info = Menu.menu_auth();
    if session.auth_user(auth_info[0], auth_info[1]):
        opt = Menu.authorize(session.logged_user)
        if opt == '1':
            # NO INPUTS HERE, PLEASE... HEAD TO MENU
            print('start flow book an appointment')
            pass
        elif opt == '2.1':
            doc_login = Menu.get_doctor()
            new_user = User(doc_login, None, None)
            find_doc = Doctor(new_user, None, None, None, None )
            new_doctor = find_doc.findDoctor(per)
            logging.info('Doctor found! Collecting the actions from the client!')
            doc_opt = Menu.doctor_option(new_doctor)
        elif opt == '2.2':
            # NO INPUTS HERE, PLEASE... HEAD TO MENU
            new_doctor = Menu.get_new_doctor()
            new_doctor.save_new_doctor(per)
            new_doctor.generateAndSaveCalendar(per)
            logging.info('\n ---The new doctor ' + new_doctor.user.login + ' Successfully created! ---')
            print('\n --- The new doctor ' + new_doctor.user.login + ' Successfully created! ---')
        elif opt == '2.3':
            pass
        elif opt == '3.1':
            pass
        elif opt == '3.2':
            pass
        elif opt == '4':
            pass
        else:
            raise IndexError("Invalid option selected")

except Exception as e:
    logging.error("Login Error: USER OR PASSWORD NOT FOUND! Try again...")
    exit(0)
except IndexError as e:
    logging.error("Data input format is invalid")
    exit(0)
