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

    def test_t2(self):
        self.buildTested = 0
        self.testItem = db.getItem("Vespa II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBoost = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_augmented(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Augmented' Vespa")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBoost = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_t1(self):
        self.buildTested = 0
        self.testItem = db.getItem("Vespa I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Dragonfly")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)
