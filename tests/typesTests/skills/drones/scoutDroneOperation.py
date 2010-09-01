import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestScoutDroneOperation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Scout Drone Operation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_droneControlRange_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Vigil"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "droneControlRange"
        skillBonus = self.skill.getAttribute("droneRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_droneControlRange_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Chimera"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "droneControlRange"
        skillBonus = self.skill.getAttribute("droneRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_droneControlRange_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Ibis"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "droneControlRange"
        skillBonus = self.skill.getAttribute("droneRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)
