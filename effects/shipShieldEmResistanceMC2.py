#Item: Broadsword [Ship]
from customEffects import boost
def shipShieldEmResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusMC2", self.item,
          extraMult = level)