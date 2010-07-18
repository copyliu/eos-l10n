#Item: Legion Offensive - Drone Synthesis Projector [Subsystem]
from customEffects import boostDroneListByReq
def subsystemBonusAmarrOffensiveDroneDamageMultiplier(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "subsystemBonusAmarrOffensive",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)