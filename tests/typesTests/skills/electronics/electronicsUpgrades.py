import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestElectronicsUpgrades(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Electronics Upgrades")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_cpu_sensorBackupArray(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Hound"))
        self.testItem = db.getItem("Multi Sensor Firewall")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_sensorBackupArrayBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Absolution"))
        self.testItem = db.getItem("F-42 Reiterative Multi-Frequency Backup Sensors")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_signalAmplifier(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Stiletto"))
        self.testItem = db.getItem("Signal Amplifier II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_signalAmplifierBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Ares"))
        self.testItem = db.getItem("F-90 Positional Signal Amplifier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_other(self):
        self.buildTested = 0
        self.testItem = db.getItem("Indirect Target Acquisition I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
