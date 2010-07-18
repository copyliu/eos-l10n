#Item: Hardwiring - Zainou 'Gnome' KZA1000 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KZA2000 [Implant]
#Item: Hardwiring - Zainou 'Gnome' KZA500 [Implant]
#Item: Weapon Upgrades [Skill]
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)