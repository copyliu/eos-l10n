#Used by: Skill: Turret Destabilization
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
