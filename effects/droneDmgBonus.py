#Used by: Skill: Amarr Drone Specialization
#                Caldari Drone Specialization
#                Gallente Drone Specialization
#                Minmatar Drone Specialization
#                Heavy Drone Operation
#                Sentry Drone Interfacing
from customEffects import boostDroneListByReq
def droneDmgBonus(self, fitting, level):
    boostDroneListByReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                        lambda drone: self.item in drone.requiredSkills,
                        self.item, extraMult = level)
