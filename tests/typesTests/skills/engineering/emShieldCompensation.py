import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEmShieldCompensation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("EM Shield Compensation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.fit.ship = Ship(db.getItem("Wyvern"))

    def test_passiveBonus_shieldAmplifier(self):
        self.buildTested = 0
        self.testItem = db.getItem("Pithum A-Type Magnetic Scattering Amplifier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "emDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveBonus_shieldAmplifierBasic(self):
        self.buildTested = 0
        self.testItem = db.getItem("Azeotropic EM Ward Salubrity")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "emDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveBonus_shieldHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Domination Photon Scattering Field")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "emDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveBonus_shieldRig(self):
        self.buildTested = 0
        self.testItem = db.getItem("Medium Anti-EM Screen Reinforcer II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "emDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveBonus_other(self):
        self.buildTested = 0
        self.testItem = db.getItem("Energized Adaptive Nano Membrane I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "emDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_activeBonus_shieldHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Photon Scattering Field II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveEmDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningbonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_activeBonus_shieldHardenerCivilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Photon Scattering Field")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveEmDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningbonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_activeBonus_armorHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Ammatar Navy Armor EM Hardener")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveEmDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
