import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestRepairDroneOperation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Repair Drone Operation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_armor(self):
        self.buildTested = 0
        self.testItem = db.getItem("Heavy Armor Maintenance Bot II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "armorDamageAmount"
        skillBonus = self.skill.getAttribute("damageHP")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_shield(self):
        self.buildTested = 0
        self.testItem = db.getItem("Medium Shield Maintenance Bot I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "shieldBonus"
        skillBonus = self.skill.getAttribute("damageHP")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_moduleArmor(self):
        self.buildTested = 0
        self.testItem = db.getItem("Large Remote Armor Repair System II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "armorDamageAmount"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_moduleShield(self):
        self.buildTested = 0
        self.testItem = db.getItem("Medium Murky Shield Screen Transmitter I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "shieldBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
