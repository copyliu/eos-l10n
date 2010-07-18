#Variations of item: Large Energy Burst Aerator I (2 of 2)
#Variations of item: Medium Energy Burst Aerator I (2 of 2)
#Variations of item: Small Energy Burst Aerator I (2 of 2)
from customEffects import boostModListByReq, multiply
def energyWeaponSpeedMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name == "Energy Weapon", self.item
                      ,helper = multiply, useStackingPenalty = True)