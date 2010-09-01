import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestElectronics(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Electronics")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_cpuOutput_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Crow"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpuOutput"
        skillBonus = self.skill.getAttribute("cpuOutputBonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpuOutput_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Phoenix"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpuOutput"
        skillBonus = self.skill.getAttribute("cpuOutputBonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpuOutput_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Velator"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpuOutput"
        skillBonus = self.skill.getAttribute("cpuOutputBonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpuOutput_subsystemElectronics(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Tengu"))
        self.testItem = db.getItem("Tengu Electronics - CPU Efficiency Gate")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpuOutput"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
