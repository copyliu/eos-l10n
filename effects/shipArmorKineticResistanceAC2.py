#Variations of item: Maller (3 of 3)
from customEffects import boost
def shipArmorKineticResistanceAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusAC2",
          self.item, extraMult = level)