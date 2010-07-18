from customEffects import boost
def shipArmorExplosiveResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusMC2",
          self.item, extraMult = level)