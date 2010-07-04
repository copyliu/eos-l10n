#Used by: Ship: Ferox
#               Vulture
#               Nighthawk
from customEffects import boost
def shipShieldExplosiveResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)