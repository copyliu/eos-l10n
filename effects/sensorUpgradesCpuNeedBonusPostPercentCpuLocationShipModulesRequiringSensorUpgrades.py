#Items from group: Cyber Electronics (3 of 27)
#Items from group: Rig Electronics (6 of 30)
#Item: Electronics Upgrades
from customEffects import boostModListBySkillReq
def sensorUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringSensorUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Electronics Upgrades",
                           self.item, extraMult = level)
