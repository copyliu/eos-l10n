#Used by: Ship: Prophecy
#               Absolution
#               Damnation
from customEffects import boost
def shipArmorExplosiveResistanceABC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusBC1", self.item,
          extraMult = level)