#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Field Purger I (2 of 2) [Module]
#Variations of item: Medium Core Defence Field Purger I (2 of 2) [Module]
#Variations of item: Small Core Defence Field Purger I (2 of 2) [Module]
#Item: Sansha Modified 'Gnome' Implant [Implant]
#Item: Shield Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("shieldRechargeRate", container.getModifiedItemAttr("rechargeratebonus") * level)