#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Gunnery Implants (3 of 9)
#Item: Gunnery [Skill]
#Item: Pashan's Turret Customization Mindlink [Implant]
from customEffects import boostModListBySkillReq
def gunneryTurretSpeeBonusPostPercentSpeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "speed", "turretSpeeBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)