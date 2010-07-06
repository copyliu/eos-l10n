#Used by: Module: Drone Repair Augmentor Rigs
#          Skill: Repair Drone Operation
from customEffects import boostDroneListByReq
def repairDroneShieldBonusBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "shieldBonus", "damageHP",
                        lambda drone: drone.group.name == "Logistic Drone",
                        self.item, extraMult = level)
