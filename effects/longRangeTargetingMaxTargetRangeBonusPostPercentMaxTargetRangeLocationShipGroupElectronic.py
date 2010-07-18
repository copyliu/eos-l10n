#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Electronics Implants (3 of 6)
#Item: Long Range Targeting
from customEffects import boost
def longRangeTargetingMaxTargetRangeBonusPostPercentMaxTargetRangeLocationShipGroupElectronic(self, fitting, level = 1):
    boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, extraMult = level)