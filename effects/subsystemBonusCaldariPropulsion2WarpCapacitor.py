#Item: Tengu Propulsion - Gravitational Capacitor [Subsystem]
from customEffects import boost
def subsystemBonusCaldariPropulsion2WarpCapacitor(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "warpCapacitorNeed", "subsystemBonusCaldariPropulsion2",
          self.item, extraMult = level)