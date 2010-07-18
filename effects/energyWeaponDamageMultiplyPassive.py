#Variations of item: Large Energy Collision Accelerator I (2 of 2)
#Variations of item: Medium Energy Collision Accelerator I (2 of 2)
#Variations of item: Small Energy Collision Accelerator I (2 of 2)
from customEffects import boostModListByReq, multiply
def energyWeaponDamageMultiplyPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                      lambda mod: mod.group.name == "Energy Weapon", self.item,
                      helper = multiply, useStackingPenalty = True)