import unittest
from model import db
from model.types import Module, Fit

class TestHeatSink(unittest.TestCase):
    def setUp(self):
        self.i = db.getItem("Heat Sink II")
        self.ii = db.getItem("Heavy Modulated Energy Beam I")
        self.f = Fit()
        self.m = Module(self.i)
        self.mm = Module(self.ii)
        self.mmm = Module(self.i)
        self.f.modules.add(self.m)
        self.f.modules.add(self.mm)
        self.f.modules.add(self.mmm)
        self.f.calculateModifiedAttributes()
        
    def test_dmgBonus(self):
        original = self.ii.attributes["damageMultiplier"].value
        multiplier = self.i.attributes["damageMultiplier"].value
        expected = original * (1 + (multiplier -1) * 0.86911998)  * multiplier
        self.assertAlmostEquals(expected, self.mm.getModifiedItemAttr("damageMultiplier"), 3)
        
    def test_speedBonus(self):
        original = self.ii.attributes["speed"].value
        multiplier = self.i.attributes["speedMultiplier"].value
        expected = original * (1 + (multiplier -1) * 0.86911998)  * multiplier
        self.assertAlmostEquals(expected, self.mm.getModifiedItemAttr("speed"), 3)