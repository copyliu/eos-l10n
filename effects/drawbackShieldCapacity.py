#Used by: All electronics superiority rigs
from customEffects import boost
def drawbackShieldCapacity(self, fitting, state):
    boost(fitting.ship, "shieldCapacity", "drawback", self.item)