#Items from group: Cyber Shields (3 of 13)
#Items from group: Rig Shield (6 of 54)
#Variations of item: Medium Core Defence Charge Economizer I (2 of 2)
#Variations of item: Small Core Defence Charge Economizer I (2 of 2)
#Item: Shield Upgrades
from customEffects import boostModListByReq
def shieldUpgradesPowerNeedBonusPostPercentPowerLocationShipModulesRequiringShieldUpgrades(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "power", "powerNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)