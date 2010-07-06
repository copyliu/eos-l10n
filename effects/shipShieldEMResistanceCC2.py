#Used by: Ship: Moa
#               Onyx
#               Eagle
from customEffects import boost
def shipShieldEMResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)