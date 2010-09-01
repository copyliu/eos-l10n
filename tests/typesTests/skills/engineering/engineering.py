import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEngineering(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Engineering")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_powerOutput_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Vengeance"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "powerOutput"
        skillBonus = self.skill.getAttribute("powerEngineeringOutputBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_powerOutput_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Avatar"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "powerOutput"
        skillBonus = self.skill.getAttribute("powerEngineeringOutputBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_powerOutput_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Velator"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "powerOutput"
        skillBonus = self.skill.getAttribute("powerEngineeringOutputBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_powerOutput_subsystemEngineering(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Proteus"))
        self.testItem = db.getItem("Proteus Engineering - Supplemental Coolant Injector")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "powerOutput"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
