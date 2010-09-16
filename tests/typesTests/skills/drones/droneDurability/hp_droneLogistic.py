import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class Test(unittest.TestCase):
    def setUp(self):
        self.skill = db.getItem("Drone Durability")
        self.bonusMap = {"shieldCapacity" : "shieldCapacityBonus",
                         "armorHP" : "armorHpBonus",
                         "hp" : "hullHpBonus"}
        self.ship = db.getItem("Thanatos")
        self.item = db.getItem("Heavy Shield Maintenance Bot II")
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
        for layer in self.bonusMap:
            setattr(self, "iValEos" + layer, self.iDrone.getModifiedItemAttr(layer))
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
        for layer in self.bonusMap:
            setattr(self, "fValEos" + layer, self.fDrone.getModifiedItemAttr(layer))

    def test_init_eos_theory(self):
        # Affected
        iValTheory = ModifiedAttributeDict()
        iValTheory.original = self.iDrone.itemModifiedAttributes.original
        for layer in self.bonusMap:
            skillBonus = self.skill.getAttribute(self.bonusMap[layer])
            iValTheory.boost(layer, skillBonus * self.iSkillLvl)
            self.assertEquals(getattr(self, "iValEos" + layer), iValTheory[layer])

    def test_final_eos_theory(self):
        # Affected
        fValTheory = ModifiedAttributeDict()
        fValTheory.original = self.fDrone.itemModifiedAttributes.original
        for layer in self.bonusMap:
            skillBonus = self.skill.getAttribute(self.bonusMap[layer])
            fValTheory.boost(layer, skillBonus * self.fSkillLvl)
            self.assertEquals(getattr(self, "fValEos" + layer), fValTheory[layer])

    #def test_diff_eos_ingame(self):
    #    self.buildTested = 0
    #    iValIngame = 1.05
    #    fValIngame = 1.2
    #    dValIngame = fValIngame/iValIngame
    #    iValEos = 0
    #    fValEos = 0
    #    for layer in self.bonusMap:
    #        iValEos += getattr(self, "iValEos" + layer)
    #        fValEos += getattr(self, "fValEos" + layer)
    #    dValEos = fValEos/iValEos
    #    self.assertAlmostEquals(dValEos, dValIngame)
