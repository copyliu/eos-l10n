#Variations of item: Arbitrator (3 of 3) [Ship]
from customEffects import boostDroneListByReq
def shipBonusDroneDamageMultiplierAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusAC2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)