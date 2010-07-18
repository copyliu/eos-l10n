#Item: Tengu Propulsion - Intercalated Nanofibers [Subsystem]
#Item: Tengu Propulsion - Interdiction Nullifier [Subsystem]
from customEffects import boost
def subsystemBonusCaldariPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusCaldariPropulsion",
          self.item, extraMult = level)