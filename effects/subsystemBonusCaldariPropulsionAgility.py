#Variations of item: Tengu Propulsion - Intercalated Nanofibers (2 of 4)
from customEffects import boost
def subsystemBonusCaldariPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusCaldariPropulsion",
          self.item, extraMult = level)