import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestFighterBombers(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Fighter Bombers")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_damage_fighterAmarr(self):
        self.buildTested = 0
        self.testItem = db.getItem("Malleus")
        self.testDrone = Drone(self.testItem)
        self.testCharge = self.testDrone.charge
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedChargeAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_damage_fighterCaldari(self):
        self.buildTested = 0
        self.testItem = db.getItem("Mantis")
        self.testDrone = Drone(self.testItem)
        self.testCharge = self.testDrone.charge
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedChargeAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_damage_fighterGallente(self):
        self.buildTested = 0
        self.testItem = db.getItem("Cyclops")
        self.testDrone = Drone(self.testItem)
        self.testCharge = self.testDrone.charge
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedChargeAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_damage_fighterMinmatar(self):
        self.buildTested = 0
        self.testItem = db.getItem("Tyrfing")
        self.testDrone = Drone(self.testItem)
        self.testCharge = self.testDrone.charge
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedChargeAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)
