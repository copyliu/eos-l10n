#Used by: Ship: Dominix
#               Sin
from customEffects import boostDroneListByReq
def shipBonusDroneDamageMultiplierGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusGB2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)