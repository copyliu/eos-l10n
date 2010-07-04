#Used by: Item: Magnetic Field Stabilizer
from customEffects import boostModListByReq, multiply
import model.fitting
def hybridWeaponSpeedMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                          lambda mod: mod.group.name == "Hybrid Weapon", self.item
                          ,helper = multiply, useStackingPenalty = True)