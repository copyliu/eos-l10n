#Used by: Skill: Trajectory Analysis
#         Item : Sooth Sayer Booster
from customEffects import boostModListBySkillReq
def surgicalStrikeFalloffBonusPostPercentFalloffLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)