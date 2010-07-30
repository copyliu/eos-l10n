import unittest
from model import db
from model.types import Module, Fit, Ship, Character, Skill

class TestThrasher(unittest.TestCase):
    def setUp(self):
        self.c = Character("ThrasherTest")
        self.c.addSkill(Skill(db.getItem("Destroyers"), 5))
        self.i = db.getItem("125mm Gatling AutoCannon I")
        self.i2 = db.getItem("Heavy Modulated Energy Beam I")
        self.m = Module(self.i)
        self.m2 = Module(self.i2)
        self.f = Fit()
        self.f.ship = Ship(db.getItem("Thrasher"))
        self.f.modules.append(self.m)
        self.f.modules.append(self.m2)

    def test_turretRofPenalty(self):
        self.f.calculateModifiedAttributes()
        original1 = self.i.attributes["speed"].value
        original2 = self.i2.attributes["speed"].value
        self.assertAlmostEquals(original1 * 1.25, self.m.getModifiedItemAttr("speed"))
        self.assertAlmostEquals(original2 * 1.25, self.m2.getModifiedItemAttr("speed"))

    def test_turretMaxRangeBonus(self):
        self.f.calculateModifiedAttributes()
        original1 = self.i.attributes["maxRange"].value
        original2 = self.i2.attributes["maxRange"].value
        self.assertAlmostEquals(original1 * 1.5, self.m.getModifiedItemAttr("maxRange"))
        self.assertAlmostEquals(original2, self.m2.getModifiedItemAttr("maxRange"))

    def test_trackingBonus(self):
        self.f.character = self.c
        self.f.calculateModifiedAttributes()
        original1 = self.i.getAttribute("trackingSpeed")
        original2 = self.i2.getAttribute("trackingSpeed")
        self.assertAlmostEquals(original1 * 1.5, self.m.getModifiedItemAttr("trackingSpeed"))
        self.assertAlmostEquals(original2, self.m2.getModifiedItemAttr("trackingSpeed"))

    def test_damageBonus(self):
        self.f.character = self.c
        self.f.calculateModifiedAttributes()
        original1 = self.i.getAttribute("damageMultiplier")
        original2 = self.i2.getAttribute("damageMultiplier")
        self.assertAlmostEquals(original1 * 1.25, self.m.getModifiedItemAttr("damageMultiplier"))
        self.assertAlmostEquals(original2, self.m2.getModifiedItemAttr("damageMultiplier"))
