#Variations of item: Maller (3 of 3)
from customEffects import boost
def shipArmorThermalResistanceAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusAC2",
          self.item, extraMult = level)