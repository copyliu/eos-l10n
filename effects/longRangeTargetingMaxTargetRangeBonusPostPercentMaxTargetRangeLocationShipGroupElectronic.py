#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Electronics Implants (3 of 6)
#Item: Long Range Targeting [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("maxTargetRange", container.getModifiedItemAttr("maxTargetRangeBonus") * level)