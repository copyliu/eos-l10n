import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "maxGroupActive"
        self.skill = db.getItem("Advanced Drone Interfacing")
        self.skillBonus = 1
        self.ship = db.getItem("Thanatos")
        self.item = db.getItem("Drone Control Unit I")
        # Define inital setup
        self.iFit = Fit()
        self.iSkillLvl = 1
        self.iChar = Character("initSkills")
        self.iChar.addSkill(Skill(self.skill, self.iSkillLvl))
        self.iFit.character = self.iChar
        self.iFit.ship = Ship(self.ship)
        self.iTestMod = Module(self.item)
        self.iFit.modules.append(self.iTestMod)
        self.iFit.calculateModifiedAttributes()
        self.iEos = self.iTestMod.getModifiedItemAttr(self.targetAttrName)
        # Define final setup
        self.fFit = Fit()
        self.fSkillLvl = 4
        self.fChar = Character("finalSkills")
        self.fChar.addSkill(Skill(self.skill, self.fSkillLvl))
        self.fFit.character = self.fChar
        self.fFit.ship = Ship(self.ship)
        self.fTestMod = Module(self.item)
        self.fFit.modules.append(self.fTestMod)
        self.fFit.calculateModifiedAttributes()
        self.fEos = self.fTestMod.getModifiedItemAttr(self.targetAttrName)

    def test_init_eos_theory(self):
        # Affected by skill
        iTheory = ModifiedAttributeDict()
        iTheory.original = self.item.attributes
        iTheory.increase(self.targetAttrName, self.skillBonus * self.iSkillLvl)
        self.assertEquals(self.iEos, iTheory[self.targetAttrName])

    #def test_init_eos_ingame(self):
    #    self.buildTested = 0
    #    iIngame = 1
    #    self.assertEquals(self.iEos, iIngame)

    def test_final_eos_theory(self):
        # Affected by skill
        fTheory = ModifiedAttributeDict()
        fTheory.original = self.item.attributes
        fTheory.increase(self.targetAttrName, self.skillBonus * self.fSkillLvl)
        self.assertEquals(self.fEos, fTheory[self.targetAttrName])

    #def test_final_eos_ingame(self):
    #    self.buildTested = 0
    #    fIngame = 4
    #    self.assertEquals(self.fEos, fIngame)
