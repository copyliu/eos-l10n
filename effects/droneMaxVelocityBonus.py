#Variations of item: Large Drone Speed Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Speed Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Speed Augmentor I (2 of 2) [Module]
#Item: Drone Navigation [Skill]
from customEffects import boostDroneListBySkillReq
def droneMaxVelocityBonus(self, fitting, level = 1, state = None):
    boostDroneListBySkillReq(fitting.drones, "maxVelocity", "droneMaxVelocityBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
