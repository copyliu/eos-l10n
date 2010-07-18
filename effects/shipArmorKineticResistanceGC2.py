#Item: Phobos [Ship]
from customEffects import boost
def shipArmorKineticResistanceGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusGC2",
          self.item, extraMult = level)