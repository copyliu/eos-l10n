#Used by: Item: Sentry Damage Augmentor
from customEffects import boostDroneListBySkillReq
def sentryDroneDamageBonus(self, fitting, state):
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                             lambda skill: skill.name == "Sentry Drone Interfacing",
                             self.item, useStackingPenalty = True)