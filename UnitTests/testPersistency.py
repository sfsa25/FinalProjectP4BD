import datetime
import unittest

from pandas.io.common import file_exists

import PersistencyDDL
import PersistencyDML
from Doctor import Doctor
from Persistency import Persistency
from User import User


class PersistencyTestCases(unittest.TestCase):



    #def testInsertDoctor(self):
    #    workingdays =  ["1"]
    #    user = User("login","DOCTOR","dsdsd")
    #    doc = Doctor(user,'Cardiologist', ["Monday", "Sunday"], ["1"], 1)
    #    per = Persistency()
    #    doc.generateAndSaveCalendar(per)

    def testGetSlots(self):
        user = User("login", "DOCTOR", "dsdsd")
        doc = Doctor(user, 'Cardiologist', ["Monday", "Sunday"], ["1"], 1)
        per = Persistency()
        dat = datetime.date(2022,7, 26)

        doc.getFreeSlots(dat.strftime("%d-%m-%Y"), per);

    def testRemoveSlot(self):
        user = User("login", "DOCTOR", "dsdsd")
        doc = Doctor(user, 'Cardiologist', ["Monday", "Sunday"], ["1"], 1)
        per = Persistency()
        dat = datetime.date(2022,7, 26)

        doc.removeSlot(dat.strftime("%d-%m-%Y"), "8:9", per);

if __name__ == '__main__':
    unittest.main()
