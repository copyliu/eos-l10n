#Item: Moros [Ship]
from customEffects import boostDroneListByReq
def dreadnoughShipBonusDroneArmorHPG2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Dreadnought")
    boostDroneListByReq(fitting.drones, "armorHP", "dreadnoughtShipBonusG2",
                        lambda drone: True, self.item, extraMult = level)
