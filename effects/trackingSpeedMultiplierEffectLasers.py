#Variations of item: Large Energy Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Medium Energy Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Small Energy Metastasis Adjuster I (2 of 2) [Module]
from customEffects import boostModListByReq, multiply
def trackingSpeedMultiplierEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "trackingSpeed", "trackingSpeedMultiplier",
                      lambda mod: mod.group.name == "Energy Weapon",
                      self.item, helper = multiply)
