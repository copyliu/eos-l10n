#Item: Daredevil [Ship]
from customEffects import boostModListBySkillReq
def shipBonusPirateSmallHybridDmg(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item)