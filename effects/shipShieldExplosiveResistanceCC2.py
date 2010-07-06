#Used by: Ship: Moa
#               Onyx
#               Eagle
from customEffects import boost
def shipShieldExplosiveResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)