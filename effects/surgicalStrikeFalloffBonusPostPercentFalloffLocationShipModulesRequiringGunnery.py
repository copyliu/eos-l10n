#Items from market group: Implants & Boosters > Booster (4 of 32)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Gunnery Implants (3 of 9)
#Item: Trajectory Analysis
from customEffects import boostModListBySkillReq
def surgicalStrikeFalloffBonusPostPercentFalloffLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "falloff", "falloffBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)