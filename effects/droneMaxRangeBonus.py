#Variations of item: Large Drone Scope Chip I (2 of 2)
#Variations of item: Medium Drone Scope Chip I (2 of 2)
#Variations of item: Small Drone Scope Chip I (2 of 2)
#Item: Drone Sharpshooting
from customEffects import boostDroneListBySkillReq
def droneMaxRangeBonus(self, fitting, state = None, level = 1):
    boostDroneListBySkillReq(fitting.drones, "maxRange", "rangeSkillBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
