#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-2 [Implant]
#Item: Shaqil's Speed Enhancer [Implant]
from customEffects import boost
def implantVelocityBonus(self, fitting):
    boost(fitting.ship, "maxVelocity", "implantBonusVelocity", self.item)