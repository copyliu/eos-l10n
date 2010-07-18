#Item: Proteus Propulsion - Gravitational Capacitor
from customEffects import boost
def subsystemBonusGallentePropulsion2WarpCapacitor(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Propulsion Systems")
    boost(fitting.ship, "warpCapacitorNeed", "subsystemBonusGallentePropulsion2",
          self.item, extraMult = level)