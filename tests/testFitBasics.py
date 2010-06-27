import unittest
from ..types import Fit, Character, Module
from ..db import queries

class TestFitBasics(unittest.TestCase):
    def setUp(self):
        self.f = Fit()
        
    def test_setNotACharacter(self):
        try:
            self.f.character = 1302
        except ValueError:
            return
        self.fail("Set an invalid character, Was expecting ValueError")
        
    def test_setCharacter(self):
        self.f.character = Character()

        
    def test_addNotAModule(self):
        try:
            self.f.addModule(1302)
        except:
            return
        self.fail("Added an invalid module, was expecting a ValueError")
        
    def test_addValidModule(self):
        self.f.addModule(Module())
            
    def test_removeModuleNotExists(self):
        self.assertRaises(ValueError, self.f.removeModule, Module())
        
    def test_removeModuleExists(self):
        m = Module()
        self.f.addModule(m)
        self.f.removeModule(m)
        
    def test_addInvalidModule(self):
        self.assertRaises(ValueError, self.f.addModule, 1302)
        
    def test_removeInvalidModule(self):
        self.assertRaises(ValueError, self.f.removeModule, 1302)
        
    def test_setNotAShip(self):
        try:
            self.f.ship = queries.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Set Gamma L as ship, was expecting ValueError")
        
    def test_setShip(self):
        self.f.ship = queries.getItem("Rifter")