#Used by: Ship: Prophecy
#               Absolution
#               Damnation
from customEffects import boost
def shipArmorKineticResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)