import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestCombatDroneOperation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testCombatDroneOperation")
        self.skill = db.getItem("Combat Drone Operation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.civilianHobgoblin = Drone(db.getItem("Civilian Hobgoblin"))
        self.t1Acolyte = Drone(db.getItem("Acolyte I"))
        self.integratedValkyrie = Drone(db.getItem("'Integrated' Valkyrie"))
        self.t2Praetor = Drone(db.getItem("Praetor II"))
        self.caldariNavyWarden = Drone(db.getItem("Caldari Navy Warden"))
        self.einherji = Drone(db.getItem("Einherji"))
        self.fit.drones.append(self.civilianHobgoblin)
        self.fit.drones.append(self.t1Acolyte)
        self.fit.drones.append(self.integratedValkyrie)
        self.fit.drones.append(self.t2Praetor)
        self.fit.drones.append(self.caldariNavyWarden)
        self.fit.drones.append(self.einherji)
        self.fit.calculateModifiedAttributes()

    def test_civilian(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.civilianHobgoblin.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.civilianHobgoblin.getModifiedItemAttr(damageAttribute))

    def test_light(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t1Acolyte.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.t1Acolyte.getModifiedItemAttr(damageAttribute))

    def test_medium(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.integratedValkyrie.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.skill.getAttribute("damageMultiplierBonus") * self.skillLevel)
            self.assertAlmostEquals(expected[damageAttribute], self.integratedValkyrie.getModifiedItemAttr(damageAttribute))

    def test_heavy(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2Praetor.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.t2Praetor.getModifiedItemAttr(damageAttribute))

    def test_sentry(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.caldariNavyWarden.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.caldariNavyWarden.getModifiedItemAttr(damageAttribute))

    def test_fighter(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.einherji.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.einherji.getModifiedItemAttr(damageAttribute))
