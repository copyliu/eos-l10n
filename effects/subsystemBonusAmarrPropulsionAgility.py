#Used by: Item: Loki Defensive - Interdiction Nullifier
from customEffects import boost
def subsystemBonusAmarrPropulsionAgility(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Propulsion Systems")
    boost(fitting.ship, "agility", "subsystemBonusAmarrPropulsion",
          self.item, extraMult = level)