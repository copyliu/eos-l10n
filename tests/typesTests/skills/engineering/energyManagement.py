import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEnergyManagement(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Energy Management")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_capacitorShipNormal(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Crusader"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorCapacity"
        skillBonus = self.skill.getAttribute("capacitorCapacityBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_capacitorShipCapital(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Revelation"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorCapacity"
        skillBonus = self.skill.getAttribute("capacitorCapacityBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_capacitorShipCivilian(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Impairor"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorCapacity"
        skillBonus = self.skill.getAttribute("capacitorCapacityBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_capacitorSubsystem(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Legion"))
        self.testItem = db.getItem("Legion Engineering - Power Core Multiplier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorCapacity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_capacitorDrone(self):
        self.buildTested = 0
        self.testItem = db.getItem("Curator II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorCapacity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
