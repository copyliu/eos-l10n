#Used by: Skill: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillTpMaxRangeBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "maxRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)