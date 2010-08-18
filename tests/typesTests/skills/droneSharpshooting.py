import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneSharpshooting(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Drone Sharpshooting")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilianCombat(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_light(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Integrated' Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_medium(self):
        self.buildTested = 0
        self.testItem = db.getItem("Valkyrie I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_heavy(self):
        self.buildTested = 0
        self.testItem = db.getItem("Republic Fleet Berserker")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_sentry(self):
        self.buildTested = 0
        self.testItem = db.getItem("Caldari Navy Warden")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Templar")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_electronicWarfare(self):
        self.buildTested = 0
        self.testItem = db.getItem("Ogre SD-900")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_combatUtility(self):
        self.buildTested = 0
        self.testItem = db.getItem("Acolyte EV-300")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_logistic(self):
        self.buildTested = 0
        self.testItem = db.getItem("Heavy Shield Maintenance Bot II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_civilianMining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Mining Drone")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_mining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Mining Drone II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

