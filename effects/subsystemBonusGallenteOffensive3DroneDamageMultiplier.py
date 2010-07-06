#Used by: Item: Legion Offensive - Drone Synthesis Projector
from customEffects import boostDroneListByReq
def subsystemBonusGallenteOffensive3DroneDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Offensive Systems")
    boostDroneListByReq(fitting.drones,
                        "damageMultiplier", "subsystemBonusGallenteOffensive3",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)