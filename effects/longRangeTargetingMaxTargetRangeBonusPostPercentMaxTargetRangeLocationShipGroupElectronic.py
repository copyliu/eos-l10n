#Used by: Skill: Long Range Targeting
from customEffects import boost
def longRangeTargetingMaxTargetRangeBonusPostPercentMaxTargetRangeLocationShipGroupElectronic(self, fitting, level = 1):
    boost(fitting.ship, "maxTargetRange", "maxTargetRangeBonus", self.item, extraMult = level)