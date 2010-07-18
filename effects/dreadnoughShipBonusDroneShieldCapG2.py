#Item: Moros
from customEffects import boostDroneListByReq
def dreadnoughShipBonusDroneShieldCapG2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Dreadnought")
    boostDroneListByReq(fitting.drones, "shieldCapacity", "dreadnoughtShipBonusG2",
                        lambda drone: True, self.item, extraMult = level)