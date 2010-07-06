#Used by: Skill: Energy Grid Upgrades
#           Rig: Powergrid Subroutine Maximizer
from customEffects import boostModListBySkillReq
def energyGridUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringEnergyGridUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Energy Grid Upgrades" ,
                           self.item, extraMult = level)