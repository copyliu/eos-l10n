import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestExplosiveShieldCompensation(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Explosive Shield Compensation")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char
        self.fit.ship = Ship(db.getItem("Kronos"))

    def test_explosiveDamageResistanceBonus_shieldAmplifier(self):
        self.buildTested = 0
        self.testItem = db.getItem("Caldari Navy Explosion Dampening Amplifier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "explosiveDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_explosiveDamageResistanceBonus_shieldAmplifierBasic(self):
        self.buildTested = 0
        self.testItem = db.getItem("Basic Explosion Dampening Amplifier")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "explosiveDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_explosiveDamageResistanceBonus_shieldHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Snake Eyes Explosion Dampening Field")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "explosiveDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_explosiveDamageResistanceBonus_shieldRig(self):
        self.buildTested = 0
        self.testItem = db.getItem("Large Anti-Explosive Screen Reinforcer I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "explosiveDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_explosiveDamageResistanceBonus_other(self):
        self.buildTested = 0
        self.testItem = db.getItem("Large Anti-Explosive Pump I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "explosiveDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveExplosiveDamageResistanceBonus_shieldHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Dread Guristas Explosion Dampening Field")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveExplosiveDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningbonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveExplosiveDamageResistanceBonus_shieldHardenerCivilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Explosion Dampening Field")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveExplosiveDamageResistanceBonus"
        skillBonus = self.skill.getAttribute("hardeningbonus2")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_passiveExplosiveDamageResistanceBonus_armorHardener(self):
        self.buildTested = 0
        self.testItem = db.getItem("Armor Explosive Hardener I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "passiveExplosiveDamageResistanceBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
