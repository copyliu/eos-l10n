#Variations of item: Large Drone Durability Enhancer I (2 of 2) [Module]
#Variations of item: Medium Drone Durability Enhancer I (2 of 2) [Module]
#Variations of item: Small Drone Durability Enhancer I (2 of 2) [Module]
#Item: Drone Durability [Skill]
from customEffects import boostDroneListBySkillReq
def droneDurabilityHPBonus(self, fitting, level = 1, state = None):
    boostDroneListBySkillReq(fitting.drones, "hp", "hullHpBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
