#Items from market group: Ships > Carriers > Amarr (2 of 2)
from customEffects import boost
def carrierAmarrArmorResist2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Carrier")
    boost(fitting.ship, ("armorExplosiveDamageResonance", "armorKineticDamageResonance",
                         "armorEmDamageResonance", "armorThermalDamageResonance"),
          "carrierAmarrBonus2", self.item, extraMult = level)