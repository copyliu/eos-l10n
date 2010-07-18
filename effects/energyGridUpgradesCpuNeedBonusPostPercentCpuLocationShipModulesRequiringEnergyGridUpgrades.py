#Items from group: Cyber Engineering (3 of 21)
#Items from group: Rig Energy Grid (6 of 30)
#Item: Energy Grid Upgrades
from customEffects import boostModListBySkillReq
def energyGridUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringEnergyGridUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Energy Grid Upgrades" ,
                           self.item, extraMult = level)