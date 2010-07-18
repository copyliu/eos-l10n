#Item: Vengeance
from customEffects import boost
def eliteBonusGunshipArmorEmResistance1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boost(fitting.ship, "armorEmDamageResonance", "eliteBonusGunship1",
          self.item, extraMult = level)