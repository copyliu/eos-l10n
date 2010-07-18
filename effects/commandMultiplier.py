#Items from group: Leadership (5 of 14)
from customEffects import boostModListByReq, multiply
runTime = "early"
def commandMultiplier(self, fitting, level):
    boostModListByReq(fitting.modules, "commandBonus", level,
                      lambda mod: self.item in mod.requiredSkills,
                      helper = multiply)