import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestCombatDroneOperation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Combat Drone Operation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_light(self):
        self.buildTested = 0
        self.testItem = db.getItem("Acolyte I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_medium(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Integrated' Valkyrie")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            skillBonus = self.skill.getAttribute("damageMultiplierBonus")
            expected.boost(damageAttribute, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_heavy(self):
        self.buildTested = 0
        self.testItem = db.getItem("Praetor II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_sentry(self):
        self.buildTested = 0
        self.testItem = db.getItem("Caldari Navy Warden")
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
        self.testItem = db.getItem("Einherji")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)
