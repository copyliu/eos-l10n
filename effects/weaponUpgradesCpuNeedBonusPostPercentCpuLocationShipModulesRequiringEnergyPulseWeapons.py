#Item: Weapon Upgrades
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringEnergyPulseWeapons(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Energy Pulse Weapons",
                           self.item, extraMult = level)