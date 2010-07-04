#Used by: Item: Black Hole Effect Beacon
from customEffects import boostModListBySkillReq, multiply
type = "projected"
def systemFalloffRangeGunnery(self, fitting, state):
    boostModListBySkillReq(fitting.modules, "falloff", "fallofMultiplier",
                           lambda skill: skill.name == "Gunnery",
                           self.item, helper = multiply)