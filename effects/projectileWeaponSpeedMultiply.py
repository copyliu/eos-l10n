#Items from group: Gyrostabilizer (19 of 19)
from customEffects import boostModListByReq, multiply
import model.fitting
def projectileWeaponSpeedMultiply(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                          lambda mod: mod.group.name == "Projectile Weapon",
                          self.item ,helper = multiply, useStackingPenalty = True)