#Variations of item: Moa (4 of 4) [Ship]
from customEffects import boost
def shipShieldEMResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldEmDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)