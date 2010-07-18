#Item: Phobos [Ship]
from customEffects import boost
def shipArmorExplosiveResistanceGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusGC2",
          self.item, extraMult = level)