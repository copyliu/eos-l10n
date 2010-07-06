#Used by: Module: Drone Mining Augmentor Rigs
#          Skill: Drone Interfacting
#                 Mining Drone Operation
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
