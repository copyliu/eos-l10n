#Items from group: Cyber Electronics (3 of 27) [Implant]
#Items from group: Rig Electronics (6 of 30) [Module]
#Item: Electronics Upgrades [Skill]
from customEffects import boostModListBySkillReq
def sensorUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringSensorUpgrades(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Electronics Upgrades",
                           self.item, extraMult = level)
