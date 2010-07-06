#Used by: Skill: Electronics Upgrades
#       Implant: Hardwiring - Zainou 'Gypsy' KLB series
#        Module: Liquid Cooled Electronics Rigs
from customEffects import boostModListBySkillReq
def sensorUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringSensorUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Electronics Upgrades",
                           self.item, extraMult = level)
