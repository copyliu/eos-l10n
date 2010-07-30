#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Electronics Implants (3 of 3)
#Item: Signature Analysis [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus") * level)
