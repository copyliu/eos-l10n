#Used by: Skill: Afterburner
#          Item: Zor's Custom Navigation Link
#                Rogue EY-series hardwirings
from customEffects import boostModListBySkillReq
def afterburnerDurationBonusPostPercentDurationLocationShipModulesRequiringAfterburner(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "durationBonus", 
                           lambda skill: skill.name == "Afterburner", self.item, extraMult = level)
