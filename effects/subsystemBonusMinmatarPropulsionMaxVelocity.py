#Item: Loki Propulsion - Chassis Optimization [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarPropulsionMaxVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Propulsion Systems")
    boost(fitting.ship, "maxVelocity", "subsystemBonusMinmatarPropulsion",
          self.item, extraMult = level)