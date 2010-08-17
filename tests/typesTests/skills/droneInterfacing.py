import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
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
        self.testDrone = Drone(db.getItem("Civilian Hobgoblin"))
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

    def test_dmgBonusLight(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Warrior II"))
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

    def test_dmgBonusMedium(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("'Augmented' Hammerhead"))
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

    def test_dmgBonusHeavy(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Berserker I"))
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

    def test_dmgBonusSentry(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Garde II"))
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

    def test_dmgBonusFighter(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Firbolg"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            actual = self.testDrone.getModifiedItemAttr(damageAttribute)
            self.assertAlmostEquals(expected[damageAttribute], actual)

    def test_miningBonusCivilian(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Civilian Mining Drone"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "miningAmount"
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        skillBoost = self.skill.getAttribute("miningAmountBonus")
        expected.boost(targetAttrName, skillBoost * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_miningBonusT2(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Mining Drone II"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "miningAmount"
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        skillBoost = self.skill.getAttribute("miningAmountBonus")
        expected.boost(targetAttrName, skillBoost * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
