#Used by: Item: Hybrid Ambit Extension
from customEffects import boostModListByReq
def falloffBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, useStackingPenalty = True)