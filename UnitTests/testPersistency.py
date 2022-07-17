import unittest

from pandas.io.common import file_exists

import PersistencyDDL
import PersistencyDML
from Persistency import Persistency


class FileManager:
    pass


class PersistencyTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        per = Persistency()
        per.setup_tables(0)

    def setUp(self):
        print("setUp")

    def testPersistencyInitialization(self):
        per = Persistency()
        # Check if database is present
        self.assertEqual(file_exists(PersistencyDDL.db_path), True, "Database does not exist")
        per.setup_tables(1)
        #Check if table were created
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_user), 'User table was not properly '
                                                                                        'created')
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_doctor), 'Doctor table was not properly '
                                                                                        'created')
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_specialty), 'Specialty table was not properly '
                                                                                          'created')
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_appointment),
                             'Appointment table was not properly '
                             'created')
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_patient),
                             'Patient table was not properly '
                             'created')
        self.assertIsNotNone(per.execute_select_pandas(PersistencyDML.select_all_prescription),
                             'Prescription table was not properly '
                             'created')



if __name__ == '__main__':
    unittest.main()
