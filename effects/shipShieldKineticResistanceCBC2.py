#Used by: Ship: Ferox
#               Vulture
#               Nighthawk
from customEffects import boost
def shipShieldKineticResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)