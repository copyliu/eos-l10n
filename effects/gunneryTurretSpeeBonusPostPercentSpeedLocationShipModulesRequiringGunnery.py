#Used by: Skill: Gunnery
from customEffects import boostModListBySkillReq
def gunneryTurretSpeeBonusPostPercentSpeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "turretSpeeBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)