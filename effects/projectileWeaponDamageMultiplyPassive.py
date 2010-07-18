#Items from group: Rig Projectile Weapon (6 of 30)
from customEffects import boostModListByReq, multiply
def projectileWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, helper = multiply, useStackingPenalty = True)