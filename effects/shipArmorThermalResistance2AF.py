#Used by: Ship: Malediction
from customEffects import boost
def shipArmorThermalResistance2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonus2AF", self.item,
          extraMult = level)