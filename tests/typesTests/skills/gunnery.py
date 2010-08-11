import unittest
from eos import db
from eos.types import Fit, Skill, Module, Character

class TestGunnery(unittest.TestCase):
    def setUp(self):
        self.f = Fit()
        self.c = Character("testGunnery")
        self.f.character = self.c
        self.c.addSkill(Skill(db.getItem("Gunnery"), 5))
        self.i = db.getItem("Heavy Modulated Energy Beam I")
        self.m = Module(self.i)
        self.f.modules.append(self.m)
        self.f.calculateModifiedAttributes()

    def test_RoFBonus(self):
        original = self.i.getAttribute("speed")
        self.assertAlmostEquals(original * 0.9, self.m.getModifiedItemAttr("speed"))
