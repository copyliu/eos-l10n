#Item: Rattlesnake [Ship]
#Item: Rokh [Ship]
#Item: Scorpion Navy Issue [Ship]
from customEffects import boost
def shipBonusThermicShieldResistanceCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonus2CB",
          self.item, extraMult = level)
