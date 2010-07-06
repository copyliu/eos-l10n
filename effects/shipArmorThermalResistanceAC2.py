#Used by: Ship: Maller
#               Devoter
#               Sacrilege
from customEffects import boost
def shipArmorThermalResistanceAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusAC2",
          self.item, extraMult = level)