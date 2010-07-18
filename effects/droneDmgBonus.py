#Items from group: Drones (6 of 19) [Skill]
from customEffects import boostDroneListByReq
def droneDmgBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                        lambda drone: self.item in drone.requiredSkills,
                        self.item, extraMult = level)
