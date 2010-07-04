#Used by: T2 Ammo
from customEffects import multiply
def ammoInfluenceShipVelocity(self, fitting, containerModule):
    multiply(fitting.ship, "maxVelocity", "maxVelocityBonus", self.item)