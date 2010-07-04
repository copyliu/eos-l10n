#Used by: Module: Drone Speed Augmentor Rigs
#          Skill: Drone Navigation
from customEffects import boostDroneListBySkillReq
def droneMaxVelocityBonus(self, fitting, level = 1, state = None):
    boostDroneListBySkillReq(fitting.drones, "maxVelocity", "droneMaxVelocityBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
