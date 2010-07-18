#Variations of item: Large Polycarbon Engine Housing I (2 of 2)
#Variations of item: Medium Polycarbon Engine Housing I (2 of 2)
#Variations of item: Small Polycarbon Engine Housing I (2 of 2)
from customEffects import boost
def velocityBonusPassive(self, fitting, state):
    boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item,
          useStackingPenalty = True)