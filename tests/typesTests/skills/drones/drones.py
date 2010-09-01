import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDrones(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Drones")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_maxActiveDronesNormal(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Maller"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxActiveDrones"
        skillBonus = self.skill.getAttribute("maxActiveDroneBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxActiveDronesCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Moros"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxActiveDrones"
        skillBonus = self.skill.getAttribute("maxActiveDroneBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxActiveDronesCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Velator"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxActiveDrones"
        skillBonus = self.skill.getAttribute("maxActiveDroneBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)
