#Item: Drake [Ship]
from customEffects import boost
def shipShieldResistanceCBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boost(fitting.ship,
          ("shieldEmDamageResonance", "shieldThermalDamageResonance", "shieldExplosiveDamageResonance", "shieldKineticDamageResonance"),
          "shipBonusBC2", self.item, extraMult = level)