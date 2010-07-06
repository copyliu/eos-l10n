#Used by: Item: Drone Scope Chip Rigs
#        Skill: Drone Sharpshooting
from customEffects import boostDroneListBySkillReq
def droneMaxRangeBonus(self, fitting, state = None, level = 1):
    boostDroneListBySkillReq(fitting.drones, "maxRange", "rangeSkillBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
