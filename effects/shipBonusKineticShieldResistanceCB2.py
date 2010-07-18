#Items from group: Battleship (3 of 30) [Ship]
from customEffects import boost
def shipBonusKineticShieldResistanceCB2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonus2CB",
          self.item, extraMult = level)
