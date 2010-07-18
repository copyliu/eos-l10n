#Item: Arbitrator [Ship]
from customEffects import boostDroneListByReq
def shipBonusMiningDroneAmountPercentAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostDroneListByReq(fitting.drones, "miningAmount", "shipBonusAC2",
                        lambda drone: drone.group.name == "Mining Drone",
                        self.item, extraMult = level)