#Used by: Ship: Dominix
from customEffects import boostDroneListByReq
def shipBonusDroneHitpointsGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostDroneListByReq(fitting.drones, ("hp", "armorHP", "shieldCapacity"), "shipBonusGB2",
                        lambda drone: True, self.item, extraMult = level)