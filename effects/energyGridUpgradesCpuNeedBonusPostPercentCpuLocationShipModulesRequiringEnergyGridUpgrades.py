#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Grid Upgrades [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' GU2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' GU4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' GU8 [Implant]
from customEffects import boostModListBySkillReq
def energyGridUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringEnergyGridUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Energy Grid Upgrades" ,
                           self.item, extraMult = level)