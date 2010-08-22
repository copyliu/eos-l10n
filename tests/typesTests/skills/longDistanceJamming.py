import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestLongDistanceJamming(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Long Distance Jamming")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_ecm(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Hypnos' Ion Field ECM I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_sensorDamper(self):
        self.buildTested = 0
        self.testItem = db.getItem("Indirect Scanning Dampening Unit I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_targetPainter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Domination Target Painter")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_trackingDisruptor(self):
        self.buildTested = 0
        self.testItem = db.getItem("Tracking Disruptor II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_ecmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Rash' ECM Emission I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "ecmBurstRange"
        skillBonus = self.skill.getAttribute("rangeSkillBonus")
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
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_proplusionEwar(self):
        self.buildTested = 0
        self.testItem = db.getItem("Fleeting Propulsion Inhibitor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_weapon(self):
        self.buildTested = 0
        self.testItem = db.getItem("Shadow Serpentis Light Neutron Blaster")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_ewDrone(self):
        self.buildTested = 0
        self.testItem = db.getItem("Hornet EC-300")
        self.testDrone = Drone(self.testItem)
        self.fit.modules.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRange"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

