import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestAdvancedDroneInterfacing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testAdvancedDroneInterfacing")
        self.skill = db.getItem("Advanced Drone Interfacing")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.droneControlUnit = Module(db.getItem("Drone Control Unit I"))
        self.fit.modules.append(self.droneControlUnit)
        self.fit.calculateModifiedAttributes()

    def test_dcuMaxGroupActive(self):
        self.buildTested = 173608
        targetAttrName = "maxGroupActive"
        expected = ModifiedAttributeDict()
        expected.original = self.droneControlUnit.item.attributes
        expected.increase(targetAttrName, 1 * self.skillLevel)
        actual = self.droneControlUnit.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
