import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestAmarrDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testAmarrDroneSpecialization")
        self.skill = db.getItem("Amarr Drone Specialization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.t1Infiltrator = Drone(db.getItem("Infiltrator I"))
        self.t2Infiltrator = Drone(db.getItem("Infiltrator II"))
        self.augmentedInfiltrator = Drone(db.getItem("'Augmented' Infiltrator"))
        self.templar = Drone(db.getItem("Templar"))
        self.fit.drones.append(self.t1Infiltrator)
        self.fit.drones.append(self.t2Infiltrator)
        self.fit.drones.append(self.augmentedInfiltrator)
        self.fit.drones.append(self.templar)
        self.fit.calculateModifiedAttributes()

    def test_t2(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2Infiltrator.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t2Infiltrator.getModifiedItemAttr(damageAttribute))

    def test_augmented(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.augmentedInfiltrator.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.augmentedInfiltrator.getModifiedItemAttr(damageAttribute))

    def test_t1(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t1Infiltrator.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.t1Infiltrator.getModifiedItemAttr(damageAttribute))

    def test_fighter(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.templar.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.templar.getModifiedItemAttr(damageAttribute))
