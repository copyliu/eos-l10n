import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestMinmatarDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Minmatar Drone Specialization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_t2(self):
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

    def test_augmented(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Augmented' Warrior")
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

    def test_t1(self):
        self.buildTested = 0
        self.testItem = db.getItem("Warrior I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Einherji")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
