#Used by: Item: Projectile Metastasis Adjuster
from customEffects import boostModListByReq, multiply
def trackingSpeedMultiplierEffectProjectiles(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda mod: mod.group.name == "Projectile Weapon",
                      self.item, helper = multiply)
