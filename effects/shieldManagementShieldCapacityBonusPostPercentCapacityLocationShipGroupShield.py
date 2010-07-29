#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Field Extender I (2 of 2) [Module]
#Variations of item: Medium Core Defence Field Extender I (2 of 2) [Module]
#Variations of item: Small Core Defence Field Extender I (2 of 2) [Module]
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Management [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)
