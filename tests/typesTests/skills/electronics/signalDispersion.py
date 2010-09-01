import unittest
from eos import db
from eos.types import Fit, Character, Skill, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalDispersion(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Signal Dispersion")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_scanStrengthBonus_ecm(self):
        self.buildTested = 0
        self.testItem = db.getItem("Estamel's Modified ECM Multispectral Jammer")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        skillBonus = self.skill.getAttribute("scanSkillEwStrengthBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
            targetAttrName = "scan" + scanType + "StrengthBonus"
            expected.boost(targetAttrName, skillBonus * self.skillLevel)
            actual = self.testMod.getModifiedItemAttr(targetAttrName)
            self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanStrengthBonus_ecmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("ECM Burst II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        skillBonus = self.skill.getAttribute("scanSkillEwStrengthBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
            targetAttrName = "scan" + scanType + "StrengthBonus"
            expected.boost(targetAttrName, skillBonus * self.skillLevel)
            actual = self.testMod.getModifiedItemAttr(targetAttrName)
            self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanStrengthBonus_remoteEcmBurst(self):
        self.buildTested = 0
        self.testItem = db.getItem("Remote ECM Burst I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
            targetAttrName = "scan" + scanType + "StrengthBonus"
            actual = self.testMod.getModifiedItemAttr(targetAttrName)
            self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanStrengthBonus_droneElectronicWarfare(self):
        self.buildTested = 0
        self.testItem = db.getItem("Wasp EC-900")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
            targetAttrName = "scan" + scanType + "StrengthBonus"
            actual = self.testDrone.getModifiedItemAttr(targetAttrName)
            self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanStrengthBonus_bomb(self):
        self.buildTested = 0
        self.testItem = db.getItem("Bomb Launcher I")
        self.testCharge = db.getItem("Lockbreaker Bomb")
        self.testMod = Module(self.testItem)
        self.testMod.charge = self.testCharge
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
            targetAttrName = "scan" + scanType + "StrengthBonus"
            actual = self.testMod.getModifiedChargeAttr(targetAttrName)
            self.assertAlmostEquals(expected[targetAttrName], actual)
