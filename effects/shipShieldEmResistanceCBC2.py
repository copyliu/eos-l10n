#Variations of item: Ferox (3 of 3) [Ship]
from customEffects import boost
def shipShieldEmResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)