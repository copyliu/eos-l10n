#Used by: Ship: Prophecy
#               Absolution
#               Damnation
from customEffects import boost
def shipArmorEMResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)