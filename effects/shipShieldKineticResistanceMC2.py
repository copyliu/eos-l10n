#Item: Broadsword
from customEffects import boost
def shipShieldKineticResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonusMC2", self.item,
          extraMult = level)