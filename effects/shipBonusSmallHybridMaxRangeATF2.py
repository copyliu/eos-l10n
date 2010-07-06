#Used by: Ship: Utu
from customEffects import boostModListBySkillReq
def shipBonusSmallHybridMaxRangeATF2(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusATF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item)