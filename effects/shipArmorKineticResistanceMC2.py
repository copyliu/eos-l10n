#Used by: Ship: Mimir
from customEffects import boost
def shipArmorKineticResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusMC2",
          self.item, extraMult = level)