import unittest
from eos import db
from eos.types import Fit, Character, Skill
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestElectronicWarfareDroneInterfacing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Electronic Warfare Drone Interfacing")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.fit.calculateModifiedAttributes()

    def test_droneControlRange(self):
        self.buildTested = 0
        targetAttrName = "droneControlRange"
        skillBonus = self.skill.getAttribute("droneRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)
