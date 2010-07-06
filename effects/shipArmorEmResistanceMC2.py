#Used by: Ship: Mimir
from customEffects import boost
def shipArmorEmResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonusMC2",
          self.item, extraMult = level)