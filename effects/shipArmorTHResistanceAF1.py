#Used by: Ship: Punisher
from customEffects import boost
def shipArmorTHResistanceAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusAF",
          self.item, extraMult = level)