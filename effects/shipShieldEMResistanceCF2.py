#Variations of item: Merlin (2 of 4)
from customEffects import boost
def shipShieldEMResistanceCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusCF",
          self.item, extraMult = level)
