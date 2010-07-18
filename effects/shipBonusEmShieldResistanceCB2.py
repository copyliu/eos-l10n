#Item: Rattlesnake [Ship]
#Item: Rokh [Ship]
#Item: Scorpion Navy Issue [Ship]
from customEffects import boost
def shipBonusEmShieldResistanceCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonus2CB",
          self.item, extraMult = level)
