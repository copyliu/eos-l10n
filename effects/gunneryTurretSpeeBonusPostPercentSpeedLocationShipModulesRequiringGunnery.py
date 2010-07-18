#Item: Gunnery [Skill]
#Item: Hardwiring - Inherent Implants 'Lancer' G0-Delta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Delta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Delta [Implant]
#Item: Pashan's Turret Customization Mindlink [Implant]
from customEffects import boostModListBySkillReq
def gunneryTurretSpeeBonusPostPercentSpeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "turretSpeeBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)