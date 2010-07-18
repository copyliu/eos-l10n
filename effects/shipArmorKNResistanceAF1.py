#Item: Punisher [Ship]
from customEffects import boost
def shipArmorKNResistanceAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonusAF",
          self.item, extraMult = level)