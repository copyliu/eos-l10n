#Used by: Ship: Maller
#               Devoter
#               Sacrilege
from customEffects import boost
def shipArmorExplosiveResistanceAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusAC2",
          self.item, extraMult = level)