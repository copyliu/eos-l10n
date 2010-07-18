#Variations of item: Ferox (3 of 3) [Ship]
from customEffects import boost
def shipShieldExplosiveResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)