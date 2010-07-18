#Item: Surgical Strike [Skill]
from customEffects import boostModListByReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipGroupProjectileWeapon(self, fitting, level):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, extraMult = level)