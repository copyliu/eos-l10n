#Variations of item: Prophecy (3 of 3)
from customEffects import boost
def shipArmorKineticResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)