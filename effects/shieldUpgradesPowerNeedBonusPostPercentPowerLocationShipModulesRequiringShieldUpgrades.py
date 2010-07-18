#Items from group: Cyber Shields (3 of 13) [Implant]
#Items from group: Rig Shield (6 of 54) [Module]
#Variations of item: Medium Core Defence Charge Economizer I (2 of 2) [Module]
#Variations of item: Small Core Defence Charge Economizer I (2 of 2) [Module]
#Item: Shield Upgrades [Skill]
from customEffects import boostModListByReq
def shieldUpgradesPowerNeedBonusPostPercentPowerLocationShipModulesRequiringShieldUpgrades(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "power", "powerNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)