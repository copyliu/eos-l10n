#Item: Hardwiring - Zainou 'Gnome' KTA10 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KTA100 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KTA1000 [Implant]
#Item: Weapon Upgrades [Skill]
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringMissileLauncherOperation(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)