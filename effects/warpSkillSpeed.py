#Variations of item: Large Hyperspatial Velocity Optimizer I (2 of 2)
#Variations of item: Medium Hyperspatial Velocity Optimizer I (2 of 2)
#Variations of item: Small Hyperspatial Velocity Optimizer I (2 of 2)
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-0
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-1
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-2
from customEffects import boost
def warpSkillSpeed(self, fitting, state = None):
    boost(fitting.ship, "baseWarpSpeed", "WarpSBonus", self.item)