#Item: Malediction
from customEffects import boost
def shipArmorKineticResistance2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorKineticDamageResonance", "shipBonus2AF", self.item,
          extraMult = level)