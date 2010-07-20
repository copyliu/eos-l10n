#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Electronics Implants (3 of 6)
#Item: Electronics [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("cpuOutputBonus2") * level)