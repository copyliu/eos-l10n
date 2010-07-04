#Used by: Skill: Sharpshooter
#         Item : Frentix Booster
from customEffects import boostModListBySkillReq
def sharpshooterRangeSkillBonusPostPercentMaxRangeLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "maxRange", "rangeSkillBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)