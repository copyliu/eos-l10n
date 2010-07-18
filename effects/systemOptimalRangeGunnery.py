#Items from group: Effect Beacon (6 of 38)
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemOptimalRangeGunnery(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeMultiplier",
                           lambda skill: skill.name == "Gunnery",
                           self.item, helper = multiply)