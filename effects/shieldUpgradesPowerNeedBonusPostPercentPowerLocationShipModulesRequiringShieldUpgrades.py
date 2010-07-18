#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Charge Economizer I (2 of 2) [Module]
#Variations of item: Medium Core Defence Charge Economizer I (2 of 2) [Module]
#Variations of item: Small Core Defence Charge Economizer I (2 of 2) [Module]
#Item: Shield Upgrades [Skill]
from customEffects import boostModListByReq
def shieldUpgradesPowerNeedBonusPostPercentPowerLocationShipModulesRequiringShieldUpgrades(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "power", "powerNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)