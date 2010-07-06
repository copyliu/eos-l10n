#Used by: Ship: Merlin
from customEffects import boost
def shipShieldEMResistanceCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusCF",
          self.item, extraMult = level)
