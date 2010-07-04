#Used by: Item: Tengu Propulsion - Gravitational Capacitor
from customEffects import boost
def subsystemBonusCaldariPropulsion2WarpCapacitor(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "warpCapacitorNeed", "subsystemBonusCaldariPropulsion2",
          self.item, extraMult = level)