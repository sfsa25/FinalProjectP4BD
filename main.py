import logging

from ViewControl.Menu import  Menu
from ViewControl.SessionManager import SessionManager
from Persistency import Persistency

# Initiating dependent classes
per = Persistency()
session = SessionManager(per)

# Drop all tables
#per.setup_tables(0)

# Create all tables
#per.setup_tables(1)
#per.setup_data()

try:

    auth_info = Menu.menu_auth();
    if session.auth_user(auth_info[0], auth_info[1]):

        opt = Menu.authorize(session.logged_user)

except Exception as e:
    logging.error("Login Error: USER OR PASSWORD NOT FOUND! Try again...")
    exit(0)
except IndexError as e:
    logging.error("Data input format is invalid")
    exit(0)