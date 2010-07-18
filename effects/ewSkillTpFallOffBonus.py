#Item: Frequency Modulation
from customEffects import boostModListByReq
def ewSkillTpFallOffBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "falloff", "falloffBonus",
                      lambda mod: mod.group.name == "Target Painter",
                      self.item, extraMult = level)