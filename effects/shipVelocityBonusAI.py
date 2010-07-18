#Variations of item: Bestower (2 of 2) [Ship]
#Variations of item: Sigil (2 of 2) [Ship]
from customEffects import boost
def shipVelocityBonusAI(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusAI", self.item,
          extraMult = level)