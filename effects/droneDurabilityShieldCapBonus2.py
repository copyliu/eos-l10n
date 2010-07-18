#Item: Drone Durability
from customEffects import boostDroneListBySkillReq
def droneDurabilityShieldCapBonus2(self, fitting, level):
    boostDroneListBySkillReq(fitting.drones, "shieldCapacity", "shieldCapacityBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
