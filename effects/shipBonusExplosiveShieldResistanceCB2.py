#Used by: Ship: Scorpion Navy Issue
#               Rokh
#               Rattlesnake
from customEffects import boost
def shipBonusExplosiveShieldResistanceCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonus2CB",
          self.item, extraMult = level)
