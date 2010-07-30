#Items with name like: Core Defence Field Extender (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Shield Implants (3 of 3)
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Management [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("shieldCapacityBonus") * level)
