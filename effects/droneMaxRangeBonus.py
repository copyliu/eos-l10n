#Variations of item: Large Drone Scope Chip I (2 of 2) [Module]
#Variations of item: Medium Drone Scope Chip I (2 of 2) [Module]
#Variations of item: Small Drone Scope Chip I (2 of 2) [Module]
#Item: Drone Sharpshooting [Skill]
from customEffects import boostDroneListBySkillReq
def droneMaxRangeBonus(self, fitting, state = None, level = 1):
    boostDroneListBySkillReq(fitting.drones, "maxRange", "rangeSkillBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
