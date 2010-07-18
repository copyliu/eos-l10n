#Variations of item: Large Hybrid Ambit Extension I (2 of 2)
#Variations of item: Medium Hybrid Ambit Extension I (2 of 2)
#Variations of item: Small Hybrid Ambit Extension I (2 of 2)
from customEffects import boostModListByReq
def falloffBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, useStackingPenalty = True)