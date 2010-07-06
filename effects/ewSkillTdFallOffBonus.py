#Used by: Skill: Frequency Modulation
from customEffects import boostModListByReq
def ewSkillTdFallOffBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)