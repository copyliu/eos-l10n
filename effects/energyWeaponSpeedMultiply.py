#Used by: Item: Heat Sink
from customEffects import boostModListByReq, multiply
import model.fitting
def energyWeaponSpeedMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                          lambda mod: mod.group.name == "Energy Weapon", self.item
                          ,helper = multiply, useStackingPenalty = True)