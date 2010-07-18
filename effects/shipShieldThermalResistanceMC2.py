#Item: Broadsword [Ship]
from customEffects import boost
def shipShieldThermalResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusMC2", self.item,
          extraMult = level)