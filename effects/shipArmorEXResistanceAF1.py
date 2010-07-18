#Item: Punisher [Ship]
from customEffects import boost
def shipArmorEXResistanceAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonusAF",
          self.item, extraMult = level)