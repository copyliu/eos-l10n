#Used by: Item: Hybrid Locus Coordinator
from customEffects import boostModListByReq
def maxRangeBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, useStackingPenalty = True)