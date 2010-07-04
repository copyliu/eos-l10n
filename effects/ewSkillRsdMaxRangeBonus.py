#Used by: Skill: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillRsdMaxRangeBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        penalized = False
    else:
        penalized = True
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, useStackingPenalty = penalized, extraMult = level)
