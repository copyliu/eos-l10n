#Item: Surgical Strike [Skill]
from customEffects import boostModListByReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipGroupEnergyWeapon(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Energy Weapon",
                      self.item, extraMult = level)