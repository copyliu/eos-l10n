#Used by: Ship: Vigilant
from customEffects import boostModListBySkillReq
def shipHybridDmgPirateCruiser(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item)