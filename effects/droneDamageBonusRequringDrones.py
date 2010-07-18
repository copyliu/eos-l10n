#Item: Drone Interfacing
from customEffects import boostDroneListBySkillReq
def droneDamageBonusRequringDrones(self, fitting, level):
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
