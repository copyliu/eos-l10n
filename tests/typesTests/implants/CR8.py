import unittest
from model import db
from model.types import Fit, Implant, Character, Ship

class TestCR8(unittest.TestCase):
    def setUp(self):
        self.f = Fit()
        self.c = Character("testCR8")
        self.f.character = self.c
        self.f.ship = Ship(db.getItem("Rifter"))
        self.i = db.getItem("Hardwiring - Inherent Implants 'Squire' CR8")
        self.implant = Implant(self.i)
        self.f.implants.add(self.implant)
        self.f.calculateModifiedAttributes()
        
    def test_rechargeTimeBonus(self):
        original = self.f.ship.item.getAttribute("rechargeRate")
        self.assertAlmostEquals(original * 0.95, self.f.ship.getModifiedItemAttr("rechargeRate"))