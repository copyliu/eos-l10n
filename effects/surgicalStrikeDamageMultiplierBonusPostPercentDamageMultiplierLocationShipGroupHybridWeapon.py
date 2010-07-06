#Used by: Skill: Surgical Strike
from customEffects import boostModListByReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipGroupHybridWeapon(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, extraMult = level)