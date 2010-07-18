#Variations of item: Vexor (3 of 4) [Ship]
#Item: Gila [Ship]
from customEffects import boostDroneListByReq
def shipBonusDroneDamageMultiplierGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusGC2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)
