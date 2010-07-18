#Item: Punisher
from customEffects import boost
def shipArmorEMResistanceAF1(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonusAF",
          self.item, extraMult = level)