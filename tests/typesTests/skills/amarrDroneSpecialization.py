import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestAmarrDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Amarr Drone Specialization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_t2(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Infiltrator II"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBoost = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_augmented(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("'Augmented' Infiltrator"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBoost = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_t1(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Infiltrator I"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Templar"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)
