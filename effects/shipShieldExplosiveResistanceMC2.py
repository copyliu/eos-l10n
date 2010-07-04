#Used by: Ship: Broadsword
from customEffects import boost
def shipShieldExplosiveResistanceMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusMC2", self.item,
          extraMult = level)