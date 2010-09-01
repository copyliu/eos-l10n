import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignatureAnalysis(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Signature Analysis")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_scanResolution_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Incursus"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "scanResolution"
        skillBonus = self.skill.getAttribute("scanResolutionBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanResolution_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Avatar"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "scanResolution"
        skillBonus = self.skill.getAttribute("scanResolutionBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanResolution_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Impairor"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "scanResolution"
        skillBonus = self.skill.getAttribute("scanResolutionBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpuOutput_subsystemElectronics(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Proteus"))
        self.testItem = db.getItem("Proteus Electronics - CPU Efficiency Gate")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "scanResolution"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
