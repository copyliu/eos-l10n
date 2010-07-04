#Used by: Item: Projectile Collision Accelerator
from customEffects import boostModListByReq, multiply
def projectileWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, helper = multiply, useStackingPenalty = True)