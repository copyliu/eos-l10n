#Variations of item: Moa (4 of 4)
from customEffects import boost
def shipShieldThermalResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldThermalDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)