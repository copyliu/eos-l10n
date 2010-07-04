#Used by: Skill: Shield Upgrades
#         Item : Core Defence Charge Economizer
from customEffects import boostModListByReq
def shieldUpgradesPowerNeedBonusPostPercentPowerLocationShipModulesRequiringShieldUpgrades(self, fitting, state = None, level = 1):
    boostModListByReq(fitting.modules, "power", "powerNeedBonus",
                      lambda mod: self.item in mod.requiredSkills,
                      self.item, extraMult = level)