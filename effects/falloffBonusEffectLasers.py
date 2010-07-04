#Used by: Item: Energy Ambit Extension
from customEffects import boostModListByReq
def falloffBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Energy Weapon",
                      self.item, useStackingPenalty = True)