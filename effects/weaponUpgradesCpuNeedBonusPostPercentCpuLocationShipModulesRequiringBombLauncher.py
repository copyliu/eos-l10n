#Item: Weapon Upgrades [Skill]
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringBombLauncher(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Bomb Deployment",
                           self.item, extraMult = level)