#Variations of item: Large Energy Locus Coordinator I (2 of 2)
#Variations of item: Medium Energy Locus Coordinator I (2 of 2)
#Variations of item: Small Energy Locus Coordinator I (2 of 2)
from customEffects import boostModListByReq
def maxRangeBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Energy Weapon", 
                      self.item, useStackingPenalty = True)