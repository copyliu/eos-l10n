#Item: Tengu Propulsion - Gravitational Capacitor
from customEffects import boost
def subsystemBonusCaldariPropulsionWarpSpeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "baseWarpSpeed", "subsystemBonusCaldariPropulsion",
          self.item, extraMult = level)