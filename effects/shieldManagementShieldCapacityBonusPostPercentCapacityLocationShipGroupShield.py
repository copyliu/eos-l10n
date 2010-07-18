#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Field Extender I (2 of 2) [Module]
#Variations of item: Medium Core Defence Field Extender I (2 of 2) [Module]
#Variations of item: Small Core Defence Field Extender I (2 of 2) [Module]
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Management [Skill]
from customEffects import boost
def shieldManagementShieldCapacityBonusPostPercentCapacityLocationShipGroupShield(self, fitting, state = None, level = 1):
    boost(fitting.ship, "shieldCapacity", "shieldCapacityBonus",
          self.item, extraMult = level)