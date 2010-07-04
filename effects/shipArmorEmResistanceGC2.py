#Used by: Ship: Phobos
from customEffects import boost
def shipArmorEmResistanceGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonusGC2",
          self.item, extraMult = level)