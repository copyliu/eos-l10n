#Used by: Skill: Long Distance Jamming
#         Item : Centurion Implant Set
from customEffects import boostModListByReq
def ewSkillEwMaxRangeBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill" or self.item.group.category.name == "Implant":
        penalized = False
    else:
        penalized = True
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "ECM", self.item,
                      useStackingPenalty = penalized, extraMult = level)
