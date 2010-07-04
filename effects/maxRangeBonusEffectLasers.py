#Used by: Item: Energy Locus Coordinator
from customEffects import boostModListByReq
def maxRangeBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Energy Weapon", 
                      self.item, useStackingPenalty = True)