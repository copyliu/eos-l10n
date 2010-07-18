#Variations of item: Large Drone Repair Augmentor I (2 of 2)
#Variations of item: Medium Drone Repair Augmentor I (2 of 2)
#Variations of item: Small Drone Repair Augmentor I (2 of 2)
#Item: Repair Drone Operation
from customEffects import boostDroneListByReq
def repairDroneArmorDamageAmountBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "armorDamageAmount", "damageHP",
                        lambda drone: drone.group.name == "Logistic Drone",
                        self.item, extraMult = level)
