#Used by: Ship: Impel
#               Occator
from customEffects import boost
def zColinArmorHPPerLvl(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boost(fitting.ship, "armorHP", "shipBonusHPExtender1", self.item,
          extraMult = level)