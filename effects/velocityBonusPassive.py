#Used by: Item: Polycarbon Engine Housing
from customEffects import boost
def velocityBonusPassive(self, fitting, state):
    boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item,
          useStackingPenalty = True)