#Items from group: Transport Ship (2 of 8) [Ship]
from customEffects import boost
def zColinArmorHPPerLvl(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boost(fitting.ship, "armorHP", "shipBonusHPExtender1", self.item,
          extraMult = level)