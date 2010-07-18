#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Emission Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' EE2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EE4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EE8 [Implant]
from customEffects import boostModListBySkillReq
def energyEmmisionSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringEnergyEmmisionSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Energy Emission Systems",
                           self.item, extraMult = level)