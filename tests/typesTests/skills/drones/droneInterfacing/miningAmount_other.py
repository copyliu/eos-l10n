import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "miningAmount"
        self.skill = db.getItem("Drone Interfacing")
        self.ship = db.getItem("Ferox")
        self.item = db.getItem("Miner II")
        # Define initial setup
        self.iFit = Fit()
        self.iSkillLvl = 1
        self.iChar = Character("initSkills")
        self.iChar.addSkill(Skill(self.skill, self.iSkillLvl))
        self.iFit.character = self.iChar
        self.iFit.ship = Ship(self.ship)
        self.iMod = Module(self.item)
        self.iFit.modules.append(self.iMod)
        self.iFit.calculateModifiedAttributes()
        self.iValEos = self.iMod.getModifiedItemAttr(self.targetAttrName)
        # Define final setup
        self.fFit = Fit()
        self.fSkillLvl = 4
        self.fChar = Character("finalSkills")
        self.fChar.addSkill(Skill(self.skill, self.fSkillLvl))
        self.fFit.character = self.fChar
        self.fFit.ship = Ship(self.ship)
        self.fMod = Module(self.item)
        self.fFit.modules.append(self.fMod)
        self.fFit.calculateModifiedAttributes()
        self.fValEos = self.fMod.getModifiedItemAttr(self.targetAttrName)

    def test_init_eos_theory(self):
        # Not affected
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.iMod.itemModifiedAttributes.original
        self.assertEquals(self.iValEos, iValTheory[self.targetAttrName])

    def test_final_eos_theory(self):
        # Not affected
        fValTheory = ModifiedAttributeDict()
        fValTheory.original = self.fMod.itemModifiedAttributes.original
        self.assertEquals(self.fValEos, fValTheory[self.targetAttrName])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 0
    #    fValIngame = 0
    #    dValIngame = fValIngame/iValIngame
    #    dValEos = self.fValEos/self.iValEos
    #    self.assertEquals(dValEos, dValIngame)