#Used by: Ship: Moros
from customEffects import boostDroneListByReq
def dreadnoughtShipBonusDroneDamageMultiplierG2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Dreadnought")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "dreadnoughtShipBonusG2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)