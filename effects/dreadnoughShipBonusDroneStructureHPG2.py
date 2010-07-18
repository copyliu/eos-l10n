#Item: Moros [Ship]
from customEffects import boostDroneListByReq
def dreadnoughShipBonusDroneStructureHPG2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Dreadnought")
    boostDroneListByReq(fitting.drones, "hp", "dreadnoughtShipBonusG2",
                        lambda drone: True, self.item, extraMult = level)