#Used by: Ship: Archon
from customEffects import boost
def carrierCaldariShieldResist2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Carrier")
    boost(fitting.ship, ("shieldExplosiveDamageResonance", "shieldKineticDamageResonance",
                         "shieldEmDamageResonance", "shieldThermalDamageResonance"),
          "carrierCaldariBonus2", self.item, extraMult = level)