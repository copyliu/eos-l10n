#Used by: Ship: Vengeance
from customEffects import boost
def eliteBonusGunshipArmorKineticResistance1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boost(fitting.ship, "armorKineticDamageResonance", "eliteBonusGunship1",
          self.item, extraMult = level)