#Items from group: Magnetic Field Stabilizer (19 of 20) [Module]
from customEffects import boostModListByReq, multiply
import model.fitting
def hybridWeaponDamageMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                          lambda mod: mod.group.name == "Hybrid Weapon", self.item,
                          helper = multiply, useStackingPenalty = True)