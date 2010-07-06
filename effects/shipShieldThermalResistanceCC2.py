#Used by: Ship: Moa
#               Onyx
#               Eagle
from customEffects import boost
def shipShieldThermalResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)