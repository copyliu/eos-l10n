#Variations of item: Large Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Mining Augmentor I (2 of 2) [Module]
#Item: Drone Interfacing [Skill]
#Item: Mining Drone Operation [Skill]
from customEffects import boostDroneListByReq
def miningDroneOperationMiningAmountBonusPostPercentMiningDroneAmountPercentChar(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        boostDroneListByReq(fitting.drones, "miningAmount", "miningAmountBonus",
                            lambda drone: drone.group.name == "Mining Drone",
                            self.item, useStackingPenalty = False, extraMult = level)
    if self.item.group.category.name == "Module":
        boostDroneListByReq(fitting.drones, "miningAmount", "miningAmountBonus",
                            lambda drone: drone.group.name == "Mining Drone",
                            self.item, useStackingPenalty = True)
