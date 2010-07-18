#Items from group: Rig Electronics Superiority (48 of 48)
from customEffects import boost
def drawbackShieldCapacity(self, fitting, state):
    boost(fitting.ship, "shieldCapacity", "drawback", self.item)