#Item: Rapid Firing [Skill]
from customEffects import boostModListBySkillReq
def rapidFiringRofBonusPostPercentSpeedLocationShipModulesRequiringGunnery(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "speed", "rofBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)