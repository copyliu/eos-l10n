#Variations of item: Moa (4 of 4)
from customEffects import boost
def shipShieldExplosiveResistanceCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boost(fitting.ship, "shieldExplosiveDamageResonance", "shipBonusCC2", self.item,
          extraMult = level)