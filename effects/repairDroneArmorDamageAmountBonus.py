#Used by: Module: Drone Repair Augmentor Rigs
#          Skill: Repair Drone Operation
from customEffects import boostDroneListByReq
def repairDroneArmorDamageAmountBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "armorDamageAmount", "damageHP",
                        lambda drone: drone.group.name == "Logistic Drone",
                        self.item, extraMult = level)
