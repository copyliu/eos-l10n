#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Navigation Implants (3 of 15)
from customEffects import boost
def warpdriveoperationWarpCapacitorNeedBonusPostPercentWarpCapacitorNeedLocationShip(self, fitting):
    boost(fitting.ship, "warpCapacitorNeed", "warpCapacitorNeedBonus", self.item)