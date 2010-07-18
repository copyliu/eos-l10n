#Item: Proteus Propulsion - Gravitational Capacitor [Subsystem]
from customEffects import boost
def subsystemBonusGallentePropulsionWarpSpeed(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Propulsion Systems")
    boost(fitting.ship, "baseWarpSpeed", "subsystemBonusGallentePropulsion",
          self.item, extraMult = level)