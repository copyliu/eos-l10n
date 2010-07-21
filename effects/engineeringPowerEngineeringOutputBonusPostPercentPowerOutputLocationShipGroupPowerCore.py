#Items from group: Rig Energy Grid (6 of 30) [Module]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Engineering Implants (3 of 6)
#Item: Engineering [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("powerOutput", container.getModifiedItemAttr("powerEngineeringOutputBonus") * level)