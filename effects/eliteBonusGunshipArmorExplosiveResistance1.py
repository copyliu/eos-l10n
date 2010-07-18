#Item: Vengeance
from customEffects import boost
def eliteBonusGunshipArmorExplosiveResistance1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boost(fitting.ship, "armorExplosiveDamageResonance", "eliteBonusGunship1",
          self.item, extraMult = level)