#Item: Hardwiring - Zainou 'Deadeye' ZGA10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGA1000 [Implant]
#Item: Improved Frentix Booster [Implant]
#Item: Sharpshooter [Skill]
#Item: Standard Frentix Booster [Implant]
#Item: Strong Frentix Booster [Implant]
#Item: Synth Frentix Booster [Implant]
from customEffects import boostModListBySkillReq
def sharpshooterRangeSkillBonusPostPercentMaxRangeLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "maxRange", "rangeSkillBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)