import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneInterfacing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Drone Interfacing")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_dmgBonusCivilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_dmgBonusLight(self):
        self.buildTested = 0
        self.testItem = db.getItem("Warrior II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_dmgBonusMedium(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Augmented' Hammerhead")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_dmgBonusHeavy(self):
        self.buildTested = 0
        self.testItem = db.getItem("Berserker I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_dmgBonusSentry(self):
        self.buildTested = 0
        self.testItem = db.getItem("Garde II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_dmgBonusFighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Firbolg")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_miningBonusCivilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Mining Drone")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "miningAmount"
        skillBonus = self.skill.getAttribute("miningAmountBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_miningBonusT2(self):
        self.buildTested = 0
        self.testItem = db.getItem("Mining Drone II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "miningAmount"
        skillBonus = self.skill.getAttribute("miningAmountBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
