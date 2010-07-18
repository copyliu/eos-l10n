#Variations of item: Prophecy (3 of 3)
from customEffects import boost
def shipArmorThermResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorThermalDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)