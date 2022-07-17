import unittest

from EntryValidation import EntryValidation


class MyTestCase(unittest.TestCase):

    def testLoginValidation(self):
        self.assertTrue(EntryValidation.validateField("logintest", EntryValidation.LOGIN_PATTERN))
        self.assertFalse(EntryValidation.validateField("lo", EntryValidation.LOGIN_PATTERN))

    def testPasswordValidation(self):
        self.assertFalse(EntryValidation.validateField("pastest", EntryValidation.PASSWD_PATTERN))
        self.assertFalse(EntryValidation.validateField("99", EntryValidation.PASSWD_PATTERN))
        self.assertFalse(EntryValidation.validateField("999", EntryValidation.PASSWD_PATTERN))
        self.assertTrue(EntryValidation.validateField("9999", EntryValidation.PASSWD_PATTERN))


if __name__ == '__main__':
    unittest.main()
