import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.testSkill = db.getItem("Advanced Drone Interfacing")
        self.testShip = db.getItem("Thanatos")
        self.testItem = db.getItem("Drone Control Unit I")
        self.testAttrName = "maxGroupActive"
        # Define inital setup
        self.initFit = Fit()
        self.initSkillLvl = 1
        self.initChar = Character("initSkills")
        self.initChar.addSkill(Skill(self.testSkill, self.initSkillLvl))
        self.initFit.character = self.initChar
        self.initFit.ship = Ship(self.testShip)
        self.initTestMod = Module(self.testItem)
        self.initFit.modules.append(self.initTestMod)
        self.initFit.calculateModifiedAttributes()
        self.initEos = self.initTestMod.getModifiedItemAttr(self.testAttrName)
        # Define final setup
        self.finalFit = Fit()
        self.finalSkillLvl = 4
        self.finalChar = Character("finalSkills")
        self.finalChar.addSkill(Skill(self.testSkill, self.finalSkillLvl))
        self.finalFit.character = self.finalChar
        self.finalFit.ship = Ship(self.testShip)
        self.finalTestMod = Module(self.testItem)
        self.finalFit.modules.append(self.finalTestMod)
        self.finalFit.calculateModifiedAttributes()
        self.finalEos = self.finalTestMod.getModifiedItemAttr(self.testAttrName)

    def test_init_eos_theory(self):
        initTheory = ModifiedAttributeDict()
        initTheory.original = self.testItem.attributes
        initTheory.increase(self.testAttrName, 1 * self.initSkillLvl)
        self.assertEquals(self.initEos, initTheory[self.testAttrName])

    def test_init_eos_ingame(self):
        self.buildTested = 0
        initIngame = 1
        self.assertEquals(self.initEos, initIngame)

    def test_final_eos_theory(self):
        finalTheory = ModifiedAttributeDict()
        finalTheory.original = self.testItem.attributes
        finalTheory.increase(self.testAttrName, 1 * self.finalSkillLvl)
        self.assertEquals(self.finalEos, finalTheory[self.testAttrName])

    def test_final_eos_ingame(self):
        self.buildTested = 0
        finalIngame = 4
        self.assertEquals(self.finalEos, finalIngame)
