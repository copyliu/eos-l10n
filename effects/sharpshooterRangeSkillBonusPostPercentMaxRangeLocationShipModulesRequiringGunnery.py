#Items from market group: Implants & Boosters > Booster (4 of 32)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Gunnery Implants (3 of 9)
#Item: Sharpshooter
from customEffects import boostModListBySkillReq
def sharpshooterRangeSkillBonusPostPercentMaxRangeLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "maxRange", "rangeSkillBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)