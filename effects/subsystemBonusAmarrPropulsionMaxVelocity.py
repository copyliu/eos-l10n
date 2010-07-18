#Item: Legion Propulsion - Chassis Optimization
from customEffects import boost
def subsystemBonusAmarrPropulsionMaxVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Propulsion Systems")
    boost(fitting.ship, "maxVelocity", "subsystemBonusAmarrPropulsion",
          self.item, extraMult = level)