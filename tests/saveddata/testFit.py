import unittest
from model.types import Fit, Character, Module, Ship, Drone
from model import db

class TestFit(unittest.TestCase):
    def setUp(self):
        self.m = Module(db.getItem("Heat Sink I"))
        
    def test_setCharacter(self):
        f = Fit()
        f.character = Character("Testety")

        
    def test_addNotAModule(self):
        try:
            self.f.addModule(1302)
        except:
            return
        self.fail("Added an invalid module, was expecting a ValueError")
        
    def test_addValidModule(self):
        f = Fit()
        f.modules.add(self.m)
            
    def test_removeModuleNotExists(self):
        f = Fit()
        self.assertRaises(KeyError, f.modules.remove, self.m)
        
    def test_removeModuleExists(self):
        f = Fit()
        f.modules.add(self.m)
        f.modules.remove(self.m)
        
    def test_removeInvalidModule(self):
        f = Fit()
        self.assertRaises(KeyError, f.modules.remove, 1302)
        
    def test_setNotAShip(self):
        f = Fit()
        try:
            f.ship = Ship(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Set Gamma L as ship, was expecting ValueError")
        
    def test_setShip(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))