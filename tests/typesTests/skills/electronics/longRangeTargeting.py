import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestElectronics(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Long Range Targeting")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_maxTargetRange_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Vigil"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRange"
        skillBonus = self.skill.getAttribute("maxTargetRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetRange_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Nidhoggur"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRange"
        skillBonus = self.skill.getAttribute("maxTargetRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetRange_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Ibis"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRange"
        skillBonus = self.skill.getAttribute("maxTargetRangeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpuOutput_subsystemElectronics(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Tengu"))
        self.testItem = db.getItem("Tengu Electronics - Dissolution Sequencer")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
