#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Field Purger I (2 of 2) [Module]
#Variations of item: Medium Core Defence Field Purger I (2 of 2) [Module]
#Variations of item: Small Core Defence Field Purger I (2 of 2) [Module]
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Operation [Skill]
from customEffects import boost
def shieldOperationRechargeratebonusPostPercentRechargeRateLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldRechargeRate", "rechargeratebonus",
          self.item, extraMult = level)