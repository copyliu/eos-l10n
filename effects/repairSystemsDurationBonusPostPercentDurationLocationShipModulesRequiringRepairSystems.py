#Items from group: Cyber Armor (4 of 24)
#Items from group: Rig Armor (6 of 54)
#Variations of item: Medium Nanobot Accelerator I (2 of 2)
#Variations of item: Small Nanobot Accelerator I (2 of 2)
#Item: Repair Systems
from customEffects import boostModListBySkillReq
def repairSystemsDurationBonusPostPercentDurationLocationShipModulesRequiringRepairSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "durationSkillBonus",
                           lambda skill: skill.name == "Repair Systems",
                           self.item, extraMult = level)