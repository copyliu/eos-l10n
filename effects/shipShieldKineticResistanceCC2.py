#Variations of item: Moa (4 of 4) [Ship]
from customEffects import boost
def shipShieldKineticResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldKineticDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)