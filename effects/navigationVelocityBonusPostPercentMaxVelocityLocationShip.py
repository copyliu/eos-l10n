#Item: Low-grade Snake Alpha [Implant]
from customEffects import boost
def navigationVelocityBonusPostPercentMaxVelocityLocationShip(self, fitting):
    boost(fitting.ship, "maxVelocity", "velocityBonus", self.item)