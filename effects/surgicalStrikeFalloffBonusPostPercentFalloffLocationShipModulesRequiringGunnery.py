#Item: Hardwiring - Zainou 'Deadeye' ZGC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGC1000 [Implant]
#Item: Improved Sooth Sayer Booster [Implant]
#Item: Standard Sooth Sayer Booster [Implant]
#Item: Strong Sooth Sayer Booster [Implant]
#Item: Synth Sooth Sayer Booster [Implant]
#Item: Trajectory Analysis [Skill]
from customEffects import boostModListBySkillReq
def surgicalStrikeFalloffBonusPostPercentFalloffLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)