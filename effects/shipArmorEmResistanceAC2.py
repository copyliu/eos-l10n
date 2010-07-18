#Variations of item: Maller (3 of 3) [Ship]
from customEffects import boost
def shipArmorEmResistanceAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonusAC2",
          self.item, extraMult = level)