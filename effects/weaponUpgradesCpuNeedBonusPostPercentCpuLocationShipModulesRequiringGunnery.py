#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Gunnery Implants (3 of 12)
#Item: Weapon Upgrades
from customEffects import boostModListBySkillReq
def weaponUpgradesCpuNeedBonusPostPercentCpuLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "cpu", "cpuNeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)