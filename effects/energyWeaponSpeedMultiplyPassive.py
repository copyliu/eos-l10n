#Used by: Item: Energy Burst Aerator
from customEffects import boostModListByReq, multiply
def energyWeaponSpeedMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name == "Energy Weapon", self.item
                      ,helper = multiply, useStackingPenalty = True)