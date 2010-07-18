#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Missile Implants (3 of 9)
#Item: Weapon Upgrades
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringMissileLauncherOperation(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)