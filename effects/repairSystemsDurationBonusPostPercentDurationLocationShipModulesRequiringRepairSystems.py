#Used by: Skill: Repair Systems
#         Item : Nanobot Accelerator
from customEffects import boostModListBySkillReq
def repairSystemsDurationBonusPostPercentDurationLocationShipModulesRequiringRepairSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "duration", "durationSkillBonus",
                           lambda skill: skill.name == "Repair Systems",
                           self.item, extraMult = level)