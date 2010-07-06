#Used by: Skill: High Speed Maneuvering
from customEffects import boostModListBySkillReq
def highSpeedManuveringCapacitorNeedMultiplierPostPercentCapacitorNeedLocationShipModulesRequiringHighSpeedManuvering(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capacitorNeedMultiplier",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level)