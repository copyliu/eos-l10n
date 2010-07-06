#Used by: Item: Hybrid Metastasis Adjuster
from customEffects import boostModListByReq, multiply
def trackingSpeedMultiplierEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, helper = multiply)
