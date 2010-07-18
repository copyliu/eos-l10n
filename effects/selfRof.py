#Items from group: Missile Launcher Operation (6 of 24) [Skill]
from customEffects import boostModListByReq
def selfRof(self, fitting, level):
    boostModListByReq(fitting.modules, "speed", "rofBonus",
                           lambda mod: self.item in mod.requiredSkills,
                           self.item, extraMult = level)