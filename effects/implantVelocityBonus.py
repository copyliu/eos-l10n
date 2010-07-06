#Used by: Item: Hardwiring - 'Rogue' CY-X
#               Shaqil's Speed Enhancer
from customEffects import boost
def implantVelocityBonus(self, fitting):
    boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item)