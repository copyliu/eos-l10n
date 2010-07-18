#Variations of item: Loki Propulsion - Chassis Optimization (2 of 4)
from customEffects import boost
def subsystemBonusMinmatarPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusMinmatarPropulsion",
          self.item, extraMult = level)