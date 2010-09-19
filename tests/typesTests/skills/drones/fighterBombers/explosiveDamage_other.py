import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "explosiveDamage"
        self.skill = db.getItem("Fighter Bombers")
        self.ship = db.getItem("Typhoon")
        self.item = db.getItem("Siege Missile Launcher II")
        self.charge = db.getItem("Bane Torpedo")
        # Define initial setup
        self.iFit = Fit()
        self.iSkillLvl = 1
        self.iChar = Character("initSkills")
        self.iChar.addSkill(Skill(self.skill, self.iSkillLvl))
        self.iFit.character = self.iChar
        self.iFit.ship = Ship(self.ship)
        self.iMod = Module(self.item)
        self.iMod.charge = self.charge
        self.iFit.modules.append(self.iMod)
        self.iFit.calculateModifiedAttributes()
        self.iValEos = self.iMod.getModifiedChargeAttr(self.targetAttrName)
        # Define final setup
        self.fFit = Fit()
        self.fSkillLvl = 4
        self.fChar = Character("finalSkills")
        self.fChar.addSkill(Skill(self.skill, self.fSkillLvl))
        self.fFit.character = self.fChar
        self.fFit.ship = Ship(self.ship)
        self.fMod = Module(self.item)
        self.fMod.charge = self.charge
        self.fFit.modules.append(self.fMod)
        self.fFit.calculateModifiedAttributes()
        self.fValEos = self.fMod.getModifiedChargeAttr(self.targetAttrName)

    def test_init_eos_theory(self):
        # Not affected
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.iMod.chargeModifiedAttributes.original
        self.assertEquals(self.iValEos, iValTheory[self.targetAttrName])

    def test_final_eos_theory(self):
        # Not affected
        fValTheory = ModifiedAttributeDict()
        fValTheory.original = self.fMod.chargeModifiedAttributes.original
        self.assertEquals(self.fValEos, fValTheory[self.targetAttrName])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 0
    #    fValIngame = 0
    #    dValIngame = fValIngame/iValIngame
    #    dValEos = self.fValEos/self.iValEos
    #    self.assertEquals(dValEos, dValIngame)
