import unittest

import PersistencyDDL
from Persistency import Persistency
from os.path import exists as file_exists


class PersistencyTestCases(unittest.TestCase):

    def testPersistencyInitialization(self):
        pers = Persistency(1)
        self.assertEqual(file_exists(PersistencyDDL.usertable_path), True)


if __name__ == '__main__':
    unittest.main()
