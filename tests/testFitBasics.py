import unittest
from model.types import Fit, Character, Module
from model import db

class TestFitBasics(unittest.TestCase):
    def setUp(self):
        self.f = Fit()
        
    def test_setCharacter(self):
        self.f.character = Character("Testety")

        
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
        
    def test_removeInvalidModule(self):
        self.assertRaises(ValueError, self.f.removeModule, 1302)
        
    def test_setNotAShip(self):
        try:
            self.f.ship = db.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Set Gamma L as ship, was expecting ValueError")
        
    def test_setShip(self):
        self.f.ship = db.getItem("Rifter")