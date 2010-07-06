#Used by: Skill: Drone Durability
#          Item: Drone Durability Enhancer Rigs
from customEffects import boostDroneListBySkillReq
def droneDurabilityHPBonus(self, fitting, level = 1, state = None):
    boostDroneListBySkillReq(fitting.drones, "hp", "hullHpBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
