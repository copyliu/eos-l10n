#Item: Loki Propulsion - Intercalated Nanofibers [Subsystem]
#Item: Loki Propulsion - Interdiction Nullifier [Subsystem]
from customEffects import boost
def subsystemBonusMinmatarPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusMinmatarPropulsion",
          self.item, extraMult = level)