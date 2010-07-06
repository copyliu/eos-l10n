#Used by: Item: Heat Sink
import model.fitting
from customEffects import boostModListByReq, multiply
def energyWeaponDamageMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "damageMultiplier", "damageMultiplier", 
                          lambda mod: mod.group.name == "Energy Weapon", self.item,
                          helper = multiply, useStackingPenalty = True)