#Used by: Skill: Long Distance Jamming
from customEffects import boostModListByReq
def ewSkillEcmBurstRangeBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "ecmBurstRange", "rangeSkillBonus",
                      lambda mod: mod.group.name == "ECM Burst",
                      self.item, extraMult = level)