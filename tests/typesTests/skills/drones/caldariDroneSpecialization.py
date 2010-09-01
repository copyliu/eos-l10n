import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestCaldariDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Caldari Drone Specialization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_damageMultiplier_droneT2(self):
        self.buildTested = 0
        self.testItem = db.getItem("Vespa II")
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

    def test_damageMultiplier_droneAugmented(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Augmented' Vespa")
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

    def test_damageMultiplier_droneT1(self):
        self.buildTested = 0
        self.testItem = db.getItem("Vespa I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_damageMultiplier_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Dragonfly")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "damageMultiplier"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
