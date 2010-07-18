#Item: Malediction
from customEffects import boost
def shipArmorEmResistance2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boost(fitting.ship, "armorEmDamageResonance", "shipBonus2AF", self.item,
          extraMult = level)