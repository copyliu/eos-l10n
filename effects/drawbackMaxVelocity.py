#Items from group: Rig Armor (54 of 54)
from customEffects import boost
def drawbackMaxVelocity(self, fitting, state):
    boost(fitting.ship, "maxVelocity", "drawback", self.item, useStackingPenalty = True)