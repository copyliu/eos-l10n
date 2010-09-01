import unittest
from eos import db
from eos.types import Fit, Character, Skill, Implant, Ship, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalSuppression(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Signal Suppression")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_sensorDamper(self):
        self.buildTested = 0
        self.testItem = db.getItem("Remote Sensor Dampener I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        skillBonus = self.skill.getAttribute("scanSkillEwStrengthBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for sensorMod in ("maxTargetRangeBonus", "scanResolutionBonus"):
            expected.boost(sensorMod, skillBonus * self.skillLevel)
            actual = self.testMod.getModifiedItemAttr(sensorMod)
            self.assertAlmostEquals(expected[sensorMod], actual)

    def test_sensorBooster(self):
        self.buildTested = 0
        self.testItem = db.getItem("Shadow Serpentis Sensor Booster")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for sensorMod in ("maxTargetRangeBonus", "scanResolutionBonus"):
            actual = self.testMod.getModifiedItemAttr(sensorMod)
            self.assertAlmostEquals(expected[sensorMod], actual)

    def test_signalAmplifier(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Cruor"))
        self.testItem = db.getItem("Signal Amplifier II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for sensorMod in ("maxTargetRangeBonus", "scanResolutionBonus"):
            actual = self.testMod.getModifiedItemAttr(sensorMod)
            self.assertAlmostEquals(expected[sensorMod], actual)

    def test_remoteSensorBooster(self):
        self.buildTested = 0
        self.testItem = db.getItem("Connected Scanning I CPU Uplink")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for sensorMod in ("maxTargetRangeBonus", "scanResolutionBonus"):
            actual = self.testMod.getModifiedItemAttr(sensorMod)
            self.assertAlmostEquals(expected[sensorMod], actual)

    def test_warpCoreStabilizer(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Ferox"))
        self.testItem = db.getItem("'Halcyon' Core Equalizer I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRangeBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_mindlink(self):
        self.buildTested = 0
        self.testItem = db.getItem("Information Warfare Mindlink")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRangeBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_implantLockRange(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Harbinger"))
        self.testItem = db.getItem("Hardwiring - Zainou 'Gypsy' KPB-50")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxTargetRangeBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_implantScanRes(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Lachesis"))
        self.testItem = db.getItem("Hardwiring - Zainou 'Gypsy' KNB-25")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "scanResolutionBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
