#Variations of item: Large Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Medium Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Small Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Item: Turret Destabilization [Skill]
from customEffects import boostModListByReq
def ewSkillTrackingDisruptionMaxRangeBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill": penalized = False
    else: penalized = True
    boostModListByReq(fitting.modules, "maxRangeBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, useStackingPenalty = penalized, extraMult = level)
    boostModListByReq(fitting.modules, "falloffBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, useStackingPenalty = penalized, extraMult = level)
