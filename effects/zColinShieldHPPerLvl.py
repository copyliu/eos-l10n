#Items from group: Transport Ship (2 of 8)
from customEffects import boost
def zColinShieldHPPerLvl(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boost(fitting.ship, "shieldCapacity", "shipBonusHPExtender1", self.item,
          extraMult = level)