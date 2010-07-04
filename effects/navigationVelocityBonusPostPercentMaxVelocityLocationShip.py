#Used by: Item: Low-grade Snake Alpha
from customEffects import boost
def navigationVelocityBonusPostPercentMaxVelocityLocationShip(self, fitting):
    boost(fitting.ship, "maxVelocity", "velocityBonus", self.item)