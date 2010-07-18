#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Armor Implants (3 of 3)
#Variations of item: Large Nanobot Accelerator I (2 of 2) [Module]
#Variations of item: Medium Nanobot Accelerator I (2 of 2) [Module]
#Variations of item: Small Nanobot Accelerator I (2 of 2) [Module]
#Item: Numon Family Heirloom [Implant]
#Item: Repair Systems [Skill]
from customEffects import boostModListBySkillReq
def repairSystemsDurationBonusPostPercentDurationLocationShipModulesRequiringRepairSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "durationSkillBonus",
                           lambda skill: skill.name == "Repair Systems",
                           self.item, extraMult = level)