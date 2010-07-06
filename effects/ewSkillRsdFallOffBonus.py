#Used by: Skill: Frequency Modulation
from customEffects import boostModListByReq
def ewSkillRsdFallOffBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)