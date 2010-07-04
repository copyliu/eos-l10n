#Used by: Item: Hyperspatial Velocity Optimizer
from customEffects import boost
def warpSkillSpeed(self, fitting, state = None):
    boost(fitting.ship, "baseWarpSpeed", "WarpSBonus", self.item)