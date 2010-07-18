#Variations of item: Large Drone Durability Enhancer I (2 of 2)
#Variations of item: Medium Drone Durability Enhancer I (2 of 2)
#Variations of item: Small Drone Durability Enhancer I (2 of 2)
#Item: Drone Durability
from customEffects import boostDroneListBySkillReq
def droneDurabilityHPBonus(self, fitting, level = 1, state = None):
    boostDroneListBySkillReq(fitting.drones, "hp", "hullHpBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
