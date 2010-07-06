#Used by: Item: Tengu Propulsion - Intercalated Nanofibers
#               Tengu Propulsion - Interdiction Nullifier
from customEffects import boost
def subsystemBonusCaldariPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusCaldariPropulsion",
          self.item, extraMult = level)