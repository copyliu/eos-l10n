import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorLinking(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Sensor Linking")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_sensorDamper(self):
        self.buildTested = 0
        self.testItem = db.getItem("Remote Sensor Dampener II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        skillBonus = self.skill.getAttribute("capNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_remoteSensorBooster(self):
        self.buildTested = 0
        self.testItem = db.getItem("Linked I Sensor Network")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        skillBonus = self.skill.getAttribute("capNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_otherEwar(self):
        self.buildTested = 0
        self.testItem = db.getItem("Tracking Disruptor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
