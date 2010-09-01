import unittest
from eos import db
from eos.types import Fit, Character, Skill, Implant, Booster, Ship, Module, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignatureFocusing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Signature Focusing")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_targetPainter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Phased Weapon Navigation Array Generation Extron")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        skillBonus = self.skill.getAttribute("scanSkillTargetPaintStrengthBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_ewDrone(self):
        self.buildTested = 0
        self.testItem = db.getItem("Valkyrie TP-600")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testDrone.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_otherMod(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Executioner"))
        self.testItem = db.getItem("Inertia Stabilizers II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_implant(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Dramiel"))
        self.testItem = db.getItem("Halo Epsilon")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, expected["implantSetAngel"])
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_booster(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Kitsune"))
        self.testItem = db.getItem("Synth X-Instinct Booster")
        self.testBooster = Booster(self.testItem)
        self.fit.boosters.append(self.testBooster)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testBooster.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_charge(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Golem"))
        self.testItem = db.getItem("Siege Missile Launcher II")
        self.testCharge = db.getItem("Mjolnir Rage Torpedo")
        self.testMod = Module(self.testItem)
        self.testMod.charge = self.testCharge
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "signatureRadiusBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testCharge.attributes
        actual = self.testMod.getModifiedChargeAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
