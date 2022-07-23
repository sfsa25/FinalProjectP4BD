import logging
import unittest
from datetime import datetime as dt


from TimeTable import TimeTable


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tt = TimeTable()
        start_time = dt.now()
        rest = {}
        rest = tt.generateTimeTable(["Monday", "Tuesday", "Wednesday"], ["1", "2"])
        self.assertEqual(len(rest), 30)


if __name__ == '__main__':
    unittest.main()



