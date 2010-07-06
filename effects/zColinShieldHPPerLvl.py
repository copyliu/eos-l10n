#Used by: Ship: Mastodon
#               Bustard
from customEffects import boost
def zColinShieldHPPerLvl(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boost(fitting.ship, "shieldCapacity", "shipBonusHPExtender1", self.item,
          extraMult = level)