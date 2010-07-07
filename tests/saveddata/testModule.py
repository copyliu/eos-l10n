import unittest
from model.types import Module
from model import db

class TestModule(unittest.TestCase):
    def setUp(self):
        self.i = db.getItem("Heat Sink I")
        self.m = Module(self.i)
        
    def test_setItem(self):
        self.assertEquals(self.m.itemID, self.i.ID)
        
    def test_setWrongAmmoType(self):
        try:
            m = Module(db.getItem("125mm Gatling AutoCannon I"))
            m.charge = db.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSize(self):
        try:
            m = Module(db.getItem("Dual Light Pulse Laser I"))
            m.charge = db.getItem("Gamma M")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setWrongAmmoSubGroup(self):
        try:
            m = Module(db.getItem("Dual Light Pulse Laser I"))
            m.charge = db.getItem("Scorch S")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")
        
    def test_setCorrectAmmo(self):
        i = db.getItem("Dual Light Pulse Laser I")
        m = Module(i)
        a = db.getItem("Gamma S")
        m.charge = a
        self.assertEquals(m.itemID, i.ID)
        self.assertEquals(m.ammoID, a.ID)