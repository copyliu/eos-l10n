#Used by: Ship: Ferox
#               Vulture
#               Nighthawk
from customEffects import boost
def shipShieldThermalResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)