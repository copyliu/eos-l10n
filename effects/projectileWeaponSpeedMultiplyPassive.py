#Used by: Item: Projectile Burst Aerator
from customEffects import boostModListByReq, multiply
def projectileWeaponSpeedMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item ,helper = multiply, useStackingPenalty = True)