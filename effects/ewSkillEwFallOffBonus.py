#Used by: Skill: Frequency Modulation
from customEffects import boostModListByReq
def ewSkillEwFallOffBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)