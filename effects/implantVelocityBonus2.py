#Item: Republic Special Ops Field Enhancer - Gamma
from customEffects import boost
def implantVelocityBonus2(self, fitting):
    boost(fitting.ship, "maxVelocity", "velocityBonus2", self.item)