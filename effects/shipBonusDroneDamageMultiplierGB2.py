#Variations of item: Dominix (3 of 3) [Ship]
#Item: Rattlesnake [Ship]
from customEffects import boostDroneListByReq
def shipBonusDroneDamageMultiplierGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusGB2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)