import StaticPatterns
from EntryValidation import EntryValidation
from Persistency import Persistency


class Doctor:

    def __init__(self, user: object, specialty: object) -> object:
        self.user = user
        self.specialty = specialty

    def validate(self):
        return EntryValidation.validateField(self.specialty, StaticPatterns.SPECIALTY_PATTERN)

    def validateUser(self):
        return EntryValidation.validateField(self.user.login, StaticPatterns.LOGIN_PATTERN)

    def save_new_doctor(self, per:Persistency):
        if self.user.validate() and self.validate():
            per.insert_doctor_trans(self)

    def findDoctor(self, per:Persistency):
        if self.validateUser():
            result_find_doctor = per.findDoctor(self)

        return self;