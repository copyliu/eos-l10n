#Variations of item: Large Energy Ambit Extension I (2 of 2) [Module]
#Variations of item: Medium Energy Ambit Extension I (2 of 2) [Module]
#Variations of item: Small Energy Ambit Extension I (2 of 2) [Module]
from customEffects import boostModListByReq
def falloffBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Energy Weapon",
                      self.item, useStackingPenalty = True)