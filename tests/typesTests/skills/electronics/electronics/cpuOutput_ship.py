import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "cpuOutput"
        self.skill = db.getItem("Electronics")
        self.skillBonus = self.skill.getAttribute("cpuOutputBonus2")
        self.ship = db.getItem("Tengu")
        # Define initial setup
        self.iFit = Fit()
        self.iSkillLvl = 1
        self.iChar = Character("initSkills")
        self.iChar.addSkill(Skill(self.skill, self.iSkillLvl))
        self.iFit.character = self.iChar
        self.iFit.ship = Ship(self.ship)
        self.iFit.calculateModifiedAttributes()
        self.iValEos = self.iFit.ship.getModifiedItemAttr(self.targetAttrName)
        # Define final setup
        self.fFit = Fit()
        self.fSkillLvl = 4
        self.fChar = Character("finalSkills")
        self.fChar.addSkill(Skill(self.skill, self.fSkillLvl))
        self.fFit.character = self.fChar
        self.fFit.ship = Ship(self.ship)
        self.fFit.calculateModifiedAttributes()
        self.fValEos = self.fFit.ship.getModifiedItemAttr(self.targetAttrName)

    def test_init_eos_theory(self):
        # Affected
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.iFit.ship.itemModifiedAttributes.original
        iValTheory.boost(self.targetAttrName, self.skillBonus * self.iSkillLvl)
        self.assertEquals(self.iValEos, iValTheory[self.targetAttrName])

    def test_final_eos_theory(self):
        # Affected
        fValTheory = ModifiedAttributeDict()
        fValTheory.original = self.fFit.ship.itemModifiedAttributes.original
        fValTheory.boost(self.targetAttrName, self.skillBonus * self.fSkillLvl)
        self.assertEquals(self.fValEos, fValTheory[self.targetAttrName])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 0
    #    fValIngame = 0
    #    dValIngame = fValIngame - iValIngame
    #    dValEos = self.fValEos - self.iValEos
    #    self.assertEquals(dValEos, dValIngame)
