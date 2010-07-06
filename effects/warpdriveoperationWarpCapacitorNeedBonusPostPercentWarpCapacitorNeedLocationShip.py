#Used by: Item: Hardwiring - Eifyr & Co 'Rogue' FY-X
from customEffects import boost
def warpdriveoperationWarpCapacitorNeedBonusPostPercentWarpCapacitorNeedLocationShip(self, fitting):
    boost(fitting.ship, "warpCapacitorNeed", "warpCapacitorNeedBonus", self.item)