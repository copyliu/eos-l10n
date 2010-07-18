#Variations of item: Large Hybrid Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Medium Hybrid Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Small Hybrid Metastasis Adjuster I (2 of 2) [Module]
from customEffects import boostModListByReq, multiply
def trackingSpeedMultiplierEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda mod: mod.group.name == "Hybrid Weapon",
                      self.item, helper = multiply)
