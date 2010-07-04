#Used by: Item: Energy Collision Accelerator
from customEffects import boostModListByReq, multiply
def energyWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Energy Weapon", self.item,
                      helper = multiply, useStackingPenalty = True)