import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestCaldariDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testCaldariDroneSpecialization")
        self.skill = db.getItem("Caldari Drone Specialization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.t1Vespa = Drone(db.getItem("Vespa I"))
        self.t2Vespa = Drone(db.getItem("Vespa II"))
        self.augmentedVespa = Drone(db.getItem("'Augmented' Vespa"))
        self.dragonfly = Drone(db.getItem("Dragonfly"))
        self.fit.drones.append(self.t1Vespa)
        self.fit.drones.append(self.t2Vespa)
        self.fit.drones.append(self.augmentedVespa)
        self.fit.drones.append(self.dragonfly)
        self.fit.calculateModifiedAttributes()

    def test_t2(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2Vespa.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t2Vespa.getModifiedItemAttr(damageAttribute))

    def test_augmented(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.augmentedVespa.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.augmentedVespa.getModifiedItemAttr(damageAttribute))

    def test_t1(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t1Vespa.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.t1Vespa.getModifiedItemAttr(damageAttribute))

    def test_fighter(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.dragonfly.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.dragonfly.getModifiedItemAttr(damageAttribute))
