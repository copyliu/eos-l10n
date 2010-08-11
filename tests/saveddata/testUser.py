import unittest
from model.types import User
class TestUser(unittest.TestCase):
    def testPasswordEncryption(self):
        u = User("MOOBAR")
        u.encodeAndSetPassword("FOOBAR")
        self.assertTrue(u.isPasswordValid("FOOBAR"))
        self.assertFalse(u.isPasswordValid("FOOBUR"))
