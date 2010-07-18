#Item: Proteus Propulsion - Interdiction Nullifier
from customEffects import boost
def subsystemBonusGallentePropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusGallentePropulsion",
          self.item, extraMult = level)