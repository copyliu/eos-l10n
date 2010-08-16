import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestAmarrDroneSpecialization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testAmarrDroneSpecialization")
        self.adsi = db.getItem("Amarr Drone Specialization")
        self.adsl = 5
        self.char.addSkill(Skill(self.adsi, self.adsl))
        self.fit.character = self.char
        self.t1id = Drone(db.getItem("Infiltrator I"))
        self.t2id = Drone(db.getItem("Infiltrator II"))
        self.aid = Drone(db.getItem("'Augmented' Infiltrator"))
        self.td = Drone(db.getItem("Templar"))
        self.fit.drones.append(self.t1id)
        self.fit.drones.append(self.t2id)
        self.fit.drones.append(self.aid)
        self.fit.drones.append(self.td)
        self.fit.calculateModifiedAttributes()

    def test_t2(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2id.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.adsi.getAttribute("damageMultiplierBonus") * self.adsl)
            self.assertAlmostEquals(expected[damageAttribute], self.t2id.getModifiedItemAttr(damageAttribute))

    def test_augmented(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.aid.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            expected.boost(damageAttribute, self.adsi.getAttribute("damageMultiplierBonus") * self.adsl)
            self.assertAlmostEquals(expected[damageAttribute], self.aid.getModifiedItemAttr(damageAttribute))

    def test_t1(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t1id.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.t1id.getModifiedItemAttr(damageAttribute))

    def test_fighter(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.td.item.attributes
        for damageType in ("em", "explosive", "kinetic", "thermal"):
            damageAttribute = damageType + "Damage"
            self.assertAlmostEquals(expected[damageAttribute], self.td.getModifiedItemAttr(damageAttribute))
