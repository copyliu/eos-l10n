#Item: Abaddon
from customEffects import boost
def shipBonusArmorResistAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boost(fitting.ship, ("armorExplosiveDamageResonance", "armorKineticDamageResonance",
                         "armorEmDamageResonance", "armorThermalDamageResonance"),
          "shipBonusAB", self.item, extraMult = level)