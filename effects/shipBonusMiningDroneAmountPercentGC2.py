#Variations of item: Vexor (2 of 4)
from customEffects import boostDroneListByReq
def shipBonusMiningDroneAmountPercentGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostDroneListByReq(fitting.drones, "miningAmount", "shipBonusGC2",
                        lambda drone: drone.group.name == "Mining Drone",
                        self.item, extraMult = level)
