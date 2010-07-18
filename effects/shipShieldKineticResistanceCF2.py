#Variations of item: Merlin (2 of 4) [Ship]
from customEffects import boost
def shipShieldKineticResistanceCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonusCF", self.item,
          extraMult = level)
