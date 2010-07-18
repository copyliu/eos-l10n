#Item: Malediction [Ship]
from customEffects import boost
def shipArmorExplosiveResistance2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorExplosiveDamageResonance", "shipBonus2AF", self.item,
          extraMult = level)