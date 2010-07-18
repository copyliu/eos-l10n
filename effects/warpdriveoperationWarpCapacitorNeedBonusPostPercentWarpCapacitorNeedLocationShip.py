#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-2 [Implant]
from customEffects import boost
def warpdriveoperationWarpCapacitorNeedBonusPostPercentWarpCapacitorNeedLocationShip(self, fitting):
    boost(fitting.ship, "warpCapacitorNeed", "warpCapacitorNeedBonus", self.item)