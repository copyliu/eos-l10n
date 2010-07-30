#Items with name like: Ancillary Current Router (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Engineering Implants (3 of 6)
#Item: Engineering [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("powerEngineeringOutputBonus") * level)
