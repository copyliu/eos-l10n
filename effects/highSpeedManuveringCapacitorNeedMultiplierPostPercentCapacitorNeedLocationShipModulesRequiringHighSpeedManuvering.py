#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Navigation Implants (3 of 3)
#Item: High Speed Maneuvering [Skill]
from customEffects import boostModListBySkillReq
def highSpeedManuveringCapacitorNeedMultiplierPostPercentCapacitorNeedLocationShipModulesRequiringHighSpeedManuvering(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capacitorNeedMultiplier",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level)