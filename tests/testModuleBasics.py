import unittest
from ..types import Module
from ..db import queries

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
        self.m.item = queries.getItem("Capacitor Flux Coil I")
        
    def test_setNotAmmo(self):
        try:
            self.m.ammo = 1302
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoType(self):
        try:
            self.m.item = queries.getItem("125mm Gatling AutoCannon I")
            self.m.ammo = queries.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSize(self):
        try:
            self.m.item = queries.getItem("Dual Light Pulse Laser I")
            self.m.ammo = queries.getItem("Gamma M")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSubGroup(self):
        try:
            self.m.item = queries.getItem("Dual Light Pulse Laser I")
            self.m.ammo = queries.getItem("Scorch S")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")