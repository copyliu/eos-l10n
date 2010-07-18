#Item: Tengu Defensive - Supplemental Screening
from customEffects import boost
def subsystemBonusCaldariDefensiveShieldHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    boost(fitting.ship, "shieldCapacity", "subsystemBonusCaldariDefensive",
          self.item, extraMult = level)