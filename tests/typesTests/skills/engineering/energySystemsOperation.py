import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEnergySystemsOperation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Energy Systems Operation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_rechargeRate_ship(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Helios"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "rechargeRate"
        skillBonus = self.skill.getAttribute("capRechargeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_rechargeRate_shipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Leviathan"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "rechargeRate"
        skillBonus = self.skill.getAttribute("capRechargeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_rechargeRate_shipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Reaper"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "rechargeRate"
        skillBonus = self.skill.getAttribute("capRechargeBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_rechargeRate_subsystemEngineering(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Loki"))
        self.testItem = db.getItem("Loki Engineering - Capacitor Regeneration Matrix")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "rechargeRate"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_rechargeRate_drone(self):
        self.buildTested = 0
        self.testItem = db.getItem("Heavy Armor Maintenance Bot I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "rechargeRate"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
