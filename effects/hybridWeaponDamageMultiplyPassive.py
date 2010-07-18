#Variations of item: Large Hybrid Collision Accelerator I (2 of 2) [Module]
#Variations of item: Medium Hybrid Collision Accelerator I (2 of 2) [Module]
#Variations of item: Small Hybrid Collision Accelerator I (2 of 2) [Module]
from customEffects import boostModListByReq, multiply
def hybridWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item,
                      helper = multiply, useStackingPenalty = True)