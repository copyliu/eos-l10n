import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneInterfacing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testDroneInterfacing")
        self.skill = db.getItem("Drone Interfacing")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilian(self):
        self.buildTested = 0
        self.civilianHobgoblin = Drone(db.getItem("Civilian Hobgoblin"))
        self.fit.drones.append(self.civilianHobgoblin)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.civilianHobgoblin.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.civilianHobgoblin.getModifiedItemAttr(damageAttribute))

    def test_light(self):
        self.buildTested = 0
        self.t2Warrior = Drone(db.getItem("Warrior II"))
        self.fit.drones.append(self.t2Warrior)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.t2Warrior.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t2Warrior.getModifiedItemAttr(damageAttribute))

    def test_medium(self):
        self.buildTested = 0
        self.augmentedHammerhead = Drone(db.getItem("'Augmented' Hammerhead"))
        self.fit.drones.append(self.augmentedHammerhead)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.augmentedHammerhead.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.augmentedHammerhead.getModifiedItemAttr(damageAttribute))

    def test_heavy(self):
        self.buildTested = 0
        self.t1Berserker = Drone(db.getItem("Berserker I"))
        self.fit.drones.append(self.t1Berserker)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.t1Berserker.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t1Berserker.getModifiedItemAttr(damageAttribute))

    def test_sentry(self):
        self.buildTested = 0
        self.t2Garde = Drone(db.getItem("Garde II"))
        self.fit.drones.append(self.t2Garde)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.t2Garde.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t2Garde.getModifiedItemAttr(damageAttribute))

    def test_fighter(self):
        self.buildTested = 0
        self.firbolg = Drone(db.getItem("Firbolg"))
        self.fit.drones.append(self.firbolg)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.firbolg.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.firbolg.getModifiedItemAttr(damageAttribute))

    def test_civilianMining(self):
        self.buildTested = 0
        self.civilianMining = Drone(db.getItem("Civilian Mining Drone"))
        self.fit.drones.append(self.civilianMining)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.civilianMining.item.attributes
        expected.boost("miningAmount", self.skill.getAttribute("miningAmountBonus") * self.skillLevel)
        self.assertAlmostEquals(expected["miningAmount"], self.civilianMining.getModifiedItemAttr("miningAmount"))

    def test_mining(self):
        self.buildTested = 0
        self.t2Mining = Drone(db.getItem("Mining Drone II"))
        self.fit.drones.append(self.t2Mining)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.t2Mining.item.attributes
        expected.boost("miningAmount", self.skill.getAttribute("miningAmountBonus") * self.skillLevel)
        self.assertAlmostEquals(expected["miningAmount"], self.t2Mining.getModifiedItemAttr("miningAmount"))
