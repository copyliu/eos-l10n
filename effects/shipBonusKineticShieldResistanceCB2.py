#Used by: Ship: Scorpion Navy Issue
#               Rokh
#               Rattlesnake
from customEffects import boost
def shipBonusKineticShieldResistanceCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonus2CB",
          self.item, extraMult = level)
