import unittest
from model.types import Fit, Character, Module, User
from model import db
import hashlib

from model.db.saveddata.user import users_table

class TestSavedDataBasics(unittest.TestCase):
    def test_1getCharacter(self):
        c = db.getCharacter("TESTY")
        self.assertEquals(c.name, "TESTY")
        self.assertEquals(c.owner.username, "test")
        
    def test_2getUser(self):
        u = db.getUser("test")
        self.assertEquals(u.username, "test")
        self.assertEqual(len(u.characters), 1)
        
    def test_3addCharacter(self):
        cc = Character("Testo")
        u = db.getUser("test")
        cc.owner = u
        for char in u.characters:
            if char == cc: return
            
        self.fail("Didn't find the character we just made")
        
    def test_4addFit(self):
        u = db.getUser("test")
        f = Fit()
        f.owner = u
        f.shipID = 1 #Set a crap ID so the tests don't fail due to flushing not working due to the not null restriction
        for fit in u.fits:
            if fit == f:
                return
            
        self.fail("Didn't find the fit we just made")