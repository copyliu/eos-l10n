#Used by: Item: Hybrid Collision Accelerator
from customEffects import boostModListByReq, multiply
def hybridWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item,
                      helper = multiply, useStackingPenalty = True)