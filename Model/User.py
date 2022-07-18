import StaticPatterns
from EntryValidation import EntryValidation


class User:

    def __init__(self, login, role, passwdo):
        self.id = None
        self.login = login
        self.role = role
        self.passwd = passwdo

    def validate(self):
        log_pass = EntryValidation.validateField(self.login, StaticPatterns.LOGIN_PATTERN)
        pass_pass = EntryValidation.validateField(self.passwd, StaticPatterns.PASSWD_PATTERN)
        return log_pass and pass_pass

    def save_user(self, per):
        if self.validate():
            per.insert_user(self)
