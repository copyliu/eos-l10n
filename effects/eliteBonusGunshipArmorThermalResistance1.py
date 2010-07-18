#Item: Vengeance [Ship]
from customEffects import boost
def eliteBonusGunshipArmorThermalResistance1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boost(fitting.ship, "armorThermalDamageResonance", "eliteBonusGunship1",
          self.item, extraMult = level)