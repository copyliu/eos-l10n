import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestFrequencyModulation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Frequency Modulation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_ecm(self):
        self.buildTested = 0
        self.testItem = db.getItem("Faint Phase Inversion ECM I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        skillBonus = self.skill.getAttribute("falloffBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_sensorDamper(self):
        self.buildTested = 0
        self.testItem = db.getItem("Low Frequency Sensor Suppressor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        skillBonus = self.skill.getAttribute("falloffBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_targetPainter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Peripheral Weapon Navigation Diameter")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        skillBonus = self.skill.getAttribute("falloffBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_trackingDisruptor(self):
        self.buildTested = 0
        self.testItem = db.getItem("F-392 Baker Nunn Tracking Disruptor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        skillBonus = self.skill.getAttribute("falloffBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_ecmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("1Z-3 Subversive ECM Eruption")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_remoteEcmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("Remote ECM Burst I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_weapon(self):
        self.buildTested = 0
        self.testItem = db.getItem("200mm Railgun II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloff"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
