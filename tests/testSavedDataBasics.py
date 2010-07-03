import unittest
from model.types import Fit, Character, Module, User
from model import db
import hashlib

from model.db.saveddata.user import users_table

class TestSavedDataBasics(unittest.TestCase):
    def test_getCharacter(self):
        c = db.getCharacter("TESTY")
        self.assertEquals(c.name, "TESTY")
        self.assertEquals(c.owner.username, "test")
        
    def test_getUser(self):
        u = db.getUser("test")
        self.assertEquals(u.username, "test")
        self.assertEqual(len(u.characters), 1)