#Variations of item: Large Drone Repair Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Repair Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Repair Augmentor I (2 of 2) [Module]
#Item: Repair Drone Operation [Skill]
from customEffects import boostDroneListByReq
def repairDroneShieldBonusBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "shieldBonus", "damageHP",
                        lambda drone: drone.group.name == "Logistic Drone",
                        self.item, extraMult = level)
