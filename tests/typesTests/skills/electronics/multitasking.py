import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestMultitasking(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Multitasking")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_maxTargetsLockedFromSkills_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Moa"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetsLockedFromSkills"
        skillBonus = self.skill.getAttribute("maxTargetBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetsLockedFromSkills_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Thanatos"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetsLockedFromSkills"
        skillBonus = self.skill.getAttribute("maxTargetBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetsLockedFromSkills_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Reaper"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetsLockedFromSkills"
        skillBonus = self.skill.getAttribute("maxTargetBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.EXTRA_ATTRIBUTES
        expected.increase(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.extraAttributes[targetAttrName]
        self.assertAlmostEquals(expected[targetAttrName], actual)
