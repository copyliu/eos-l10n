#Used by: Item: Energy Burst Aerator
from customEffects import boostModListByReq, multiply
def hybridWeaponSpeedMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item
                      ,helper = multiply, useStackingPenalty = True)