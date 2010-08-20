import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestElectronicWarfare(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Electronic Warfare")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_ecm(self):
        self.buildTested = 0
        self.testItem = db.getItem("Legion ECM White Noise Generator")
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

    def test_ecmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Cetus' ECM Shockwave I")
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

    def test_remoteEcmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("Remote ECM Burst I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_otherEwar(self):
        self.buildTested = 0
        self.testItem = db.getItem("DDO Photometry Tracking Disruptor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_otherProplusionEwar(self):
        self.buildTested = 0
        self.testItem = db.getItem("True Sansha Stasis Webifier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "capacitorNeed"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
