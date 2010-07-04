#Used by: Ship: Moa
#               Onyx
#               Eagle
from customEffects import boost
def shipShieldKineticResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)