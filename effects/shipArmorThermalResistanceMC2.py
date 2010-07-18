from customEffects import boost
def shipArmorThermalResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusMC2",
          self.item, extraMult = level)