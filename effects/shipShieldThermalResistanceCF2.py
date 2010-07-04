#Used by: Ship: Merlin
from customEffects import boost
def shipShieldThermalResistanceCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusCF", self.item,
          extraMult = level)
