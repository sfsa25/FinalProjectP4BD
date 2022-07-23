from datetime import datetime

import StaticPatterns
from EntryValidation import EntryValidation
from Persistency import Persistency
from TimeTable import TimeTable


class Doctor:

    def __init__(self, user, specialty, workingdays, shifts, id):
        self.timetable = None
        self.id = id
        self.user = user
        self.specialty = specialty
        self.workingdays = workingdays
        self.shifts = shifts

    def validate(self):
        return EntryValidation.validateField(self.specialty, StaticPatterns.SPECIALTY_PATTERN)

    def generateAndSaveCalendar(self, per):
        tt = TimeTable()
        self.timetable = tt.buildTimeTable(self.workingdays, self.shifts)
        per.insertTimeTable(self.timetable, self.id)

    def validateUser(self):
        valid_login = EntryValidation.validateField(self.user.login, StaticPatterns.LOGIN_PATTERN)
        # valid_workingdays = EntryValidation.validateField(self.user.login, StaticPatterns.WORKINGDAYS)
        return valid_login

    def save_new_doctor(self, per:Persistency):
        last_id = 0
        if self.user.validate() and self.validate():
            last_id = per.insert_doctor_trans(self)
        self.id = last_id

    def findDoctor(self, per:Persistency):
        if self.validateUser():
            result_find_doctor = per.findDoctor(self)

        return self;

    def getFreeSlots(self, dat, per):
        if dat is None:
            dat = datetime.now()
        per.findDateSlots(dat)
