#Items with name like: Core Defence Field Purger (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Shield Implants (3 of 3)
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("shieldRechargeRate", container.getModifiedItemAttr("rechargeratebonus") * level)
