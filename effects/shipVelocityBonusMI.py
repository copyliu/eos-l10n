#Variations of item: Mammoth (2 of 2) [Ship]
#Variations of item: Wreathe (2 of 2) [Ship]
#Item: Hoarder [Ship]
from customEffects import boost
def shipVelocityBonusMI(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusMI", self.item,
          extraMult = level)