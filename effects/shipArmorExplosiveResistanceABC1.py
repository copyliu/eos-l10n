#Variations of item: Prophecy (3 of 3) [Ship]
from customEffects import boost
def shipArmorExplosiveResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)