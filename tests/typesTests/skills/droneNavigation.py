import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneNavigation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Drone Navigation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilianCombat(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_light(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Integrated' Hornet")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_medium(self):
        self.buildTested = 0
        self.testItem = db.getItem("Federation Navy Hammerhead")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_heavy(self):
        self.buildTested = 0
        self.testItem = db.getItem("Praetor I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Firbolg")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_fighterBomber(self):
        self.buildTested = 0
        self.testItem = db.getItem("Malleus")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_electronicWarfare(self):
        self.buildTested = 0
        self.testItem = db.getItem("Infiltrator TD-600")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_combatUtility(self):
        self.buildTested = 0
        self.testItem = db.getItem("Praetor EV-900")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_logistic(self):
        self.buildTested = 0
        self.testItem = db.getItem("Light Shield Maintenance Bot I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("droneMaxVelocityBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_civilianMining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Mining Drone")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_mining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Harvester Mining Drone")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxVelocity"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

