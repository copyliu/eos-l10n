#Variations of item: Ferox (3 of 3)
from customEffects import boost
def shipShieldThermalResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusBC2", self.item,
          extraMult = level)