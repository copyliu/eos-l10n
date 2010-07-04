#Used by: Ship: Merlin
from customEffects import boost
def shipShieldExplosiveResistanceCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusCF", self.item,
          extraMult = level)
