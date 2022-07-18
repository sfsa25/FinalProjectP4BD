import StaticPatterns
from EntryValidation import EntryValidation
from Persistency import Persistency


class Doctor:
    def __init__(self):
        self.user = None
        self.specialty = None

    def __init__(self, user, specialty):
        self.user = user
        self.specialty = specialty

    def validate(self):
        return EntryValidation.validateField(self.specialty, StaticPatterns.SPECIALTY_PATTERN)

    def save_new_doctor(self, per:Persistency):
        if self.user.validate() and self.validate():
            per.insert_doctor_trans(self)