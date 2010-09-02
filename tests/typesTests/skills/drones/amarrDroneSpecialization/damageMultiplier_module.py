import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "damageMultiplier"
        self.skill = db.getItem("Amarr Drone Specialization")
        self.skillBonus = self.skill.getAttribute("damageMultiplierBonus")
        self.ship = db.getItem("Retribution")
        self.item = db.getItem("Medium Pulse Laser II")
        # Define inital setup
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
        # Not affected by skill
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.item.attributes
        self.assertEquals(self.iValEos, iValTheory[self.targetAttrName])

    def test_final_eos_theory(self):
        # Affected by skill
        fTheory = ModifiedAttributeDict()
        fTheory.original = self.item.attributes
        self.assertEquals(self.fValEos, fTheory[self.targetAttrName])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 0
    #    fValIngame = 0
    #    dValIngame = fValIngame/iValIngame
    #    dValEos = self.fValEos/self.iValEos
    #    self.assertEquals(dValEos, dValIngame)
