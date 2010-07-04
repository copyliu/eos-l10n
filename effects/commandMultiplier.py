#Used by: Skill: X Warfare Specialist
from customEffects import boostModListByReq, multiply
runTime = "early"
def commandMultiplier(self, fitting, level):
    boostModListByReq(fitting.modules, "commandBonus", level,
                      lambda mod: self.item in mod.requiredSkills,
                      helper = multiply)