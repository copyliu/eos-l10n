#Variations of item: Large Sentry Damage Augmentor I (2 of 2)
#Variations of item: Medium Sentry Damage Augmentor I (2 of 2)
#Variations of item: Small Sentry Damage Augmentor I (2 of 2)
from customEffects import boostDroneListBySkillReq
def sentryDroneDamageBonus(self, fitting, state):
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                             lambda skill: skill.name == "Sentry Drone Interfacing",
                             self.item, useStackingPenalty = True)