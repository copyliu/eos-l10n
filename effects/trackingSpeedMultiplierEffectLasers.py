#Used by: Item: Energy Metastasis Adjuster
from customEffects import boostModListByReq, multiply
def trackingSpeedMultiplierEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda mod: mod.group.name == "Energy Weapon",
                      self.item, helper = multiply)
