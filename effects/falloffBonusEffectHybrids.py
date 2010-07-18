#Variations of item: Large Hybrid Ambit Extension I (2 of 2) [Module]
#Variations of item: Medium Hybrid Ambit Extension I (2 of 2) [Module]
#Variations of item: Small Hybrid Ambit Extension I (2 of 2) [Module]
from customEffects import boostModListByReq
def falloffBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, useStackingPenalty = True)