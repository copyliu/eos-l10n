import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.targetAttrName = "miningAmount"
        self.skill = db.getItem("Drone Interfacing")
        self.skillBonus = self.skill.getAttribute("miningAmountBonus")
        self.ship = db.getItem("Deimos")
        self.item = db.getItem("Harvester Mining Drone")
        # Define initial setup
        self.iFit = Fit()
        self.iSkillLvl = 1
        self.iChar = Character("initSkills")
        self.iChar.addSkill(Skill(self.skill, self.iSkillLvl))
        self.iFit.character = self.iChar
        self.iFit.ship = Ship(self.ship)
        self.iDrone = Drone(self.item)
        self.iFit.drones.append(self.iDrone)
        self.iFit.calculateModifiedAttributes()
        self.iValEos = self.iDrone.getModifiedItemAttr(self.targetAttrName)
        # Define final setup
        self.fFit = Fit()
        self.fSkillLvl = 4
        self.fChar = Character("finalSkills")
        self.fChar.addSkill(Skill(self.skill, self.fSkillLvl))
        self.fFit.character = self.fChar
        self.fFit.ship = Ship(self.ship)
        self.fDrone = Drone(self.item)
        self.fFit.drones.append(self.fDrone)
        self.fFit.calculateModifiedAttributes()
        self.fValEos = self.fDrone.getModifiedItemAttr(self.targetAttrName)

    def test_init_eos_theory(self):
        # Affected
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.iDrone.itemModifiedAttributes.original
        iValTheory.boost(self.targetAttrName, self.skillBonus * self.iSkillLvl)
        self.assertEquals(self.iValEos, iValTheory[self.targetAttrName])

    def test_final_eos_theory(self):
        # Affected
        fValTheory = ModifiedAttributeDict()
        fValTheory.original = self.fDrone.itemModifiedAttributes.original
        fValTheory.boost(self.targetAttrName, self.skillBonus * self.fSkillLvl)
        self.assertEquals(self.fValEos, fValTheory[self.targetAttrName])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 0
    #    fValIngame = 0
    #    dValIngame = fValIngame/iValIngame
    #    dValEos = self.fValEos/self.iValEos
    #    self.assertEquals(dValEos, dValIngame)