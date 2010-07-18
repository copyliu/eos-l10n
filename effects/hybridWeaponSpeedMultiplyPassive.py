#Variations of item: Large Hybrid Burst Aerator I (2 of 2) [Module]
#Variations of item: Medium Hybrid Burst Aerator I (2 of 2) [Module]
#Variations of item: Small Hybrid Burst Aerator I (2 of 2) [Module]
from customEffects import boostModListByReq, multiply
def hybridWeaponSpeedMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item
                      ,helper = multiply, useStackingPenalty = True)