import logging
from typing import re

from ViewControl.EntryValidation import EntryValidation
import Menu


class Menu:

    @staticmethod
    def menu_auth():
        login = input("Enter your login: \n")
        if EntryValidation.validateField(login, EntryValidation.LOGIN_PATTERN):
            passwd = input("Enter your password: ")
            if not EntryValidation.validateField(passwd, EntryValidation.PASSWD_PATTERN):
                logging.ERROR("Invalid password format. Format accepted: 4 digits")
                raise IndexError("Password format is invalid")
        else:
            logging.ERROR("Invalid login format. Format accepted: 4 to 25 string length")
            raise IndexError("Login format is invalid")

        return [login, passwd]
