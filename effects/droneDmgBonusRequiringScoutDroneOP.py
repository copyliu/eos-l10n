#Used by: Skill: Combat Drone Operation
from customEffects import boostDroneListBySkillReq
def droneDmgBonusRequiringScoutDroneOP(self, fitting, level):
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                             lambda skill: skill.name == "Scout Drone Operation",
                             self.item, extraMult = level)