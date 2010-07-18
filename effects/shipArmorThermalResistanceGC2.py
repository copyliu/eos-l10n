#Item: Phobos
from customEffects import boost
def shipArmorThermalResistanceGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusGC2",
          self.item, extraMult = level)