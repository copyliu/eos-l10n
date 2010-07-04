#Used by: Skill: Rocket Specialization
#                Standard Missile Specialization
#                Heavy Missile Specialization
#                Cruise Missile Specialization
#                Torpedo Specialization
#                Heavy Assault Missile Specialization
from customEffects import boostModListByReq
def selfRof(self, fitting, level):
    boostModListByReq(fitting.modules, "speed", "rofBonus",
                           lambda mod: self.item in mod.requiredSkills,
                           self.item, extraMult = level)