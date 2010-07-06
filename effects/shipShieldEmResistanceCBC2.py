#Used by: Ship: Ferox
#               Vulture
#               Nighthawk
from customEffects import boost
def shipShieldEmResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)