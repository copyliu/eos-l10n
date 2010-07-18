#Variations of item: Large Hybrid Locus Coordinator I (2 of 2)
#Variations of item: Medium Hybrid Locus Coordinator I (2 of 2)
#Variations of item: Small Hybrid Locus Coordinator I (2 of 2)
from customEffects import boostModListByReq
def maxRangeBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, useStackingPenalty = True)