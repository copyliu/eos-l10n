#Variations of item: Mammoth (2 of 2)
#Variations of item: Wreathe (2 of 2)
#Item: Hoarder
from customEffects import boost
def shipVelocityBonusMI(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Industrial")
    boost(fitting.ship, "maxVelocity", "shipBonusMI", self.item,
          extraMult = level)