import unittest
from model.types import Module
from model import db

class TestModuleBasics(unittest.TestCase):
    def setUp(self):
        self.m = Module()
        
    def test_setNotAnItem(self):
        try:
            self.m.item = 1302
        except ValueError:
            return
        self.fail("Expected a value error, didn't get it.")
        
    def test_setItem(self):
        self.m.item = db.getItem("Capacitor Flux Coil I")
        
    def test_setNotAmmo(self):
        try:
            self.m.ammo = 1302
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoType(self):
        try:
            self.m.item = db.getItem("125mm Gatling AutoCannon I")
            self.m.ammo = db.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSize(self):
        try:
            self.m.item = db.getItem("Dual Light Pulse Laser I")
            self.m.ammo = db.getItem("Gamma M")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSubGroup(self):
        try:
            self.m.item = db.getItem("Dual Light Pulse Laser I")
            self.m.ammo = db.getItem("Scorch S")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")