#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Armor Implants (3 of 3)
#Item: Mechanic [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.ship.boostItemAttr("hp", container.getModifiedItemAttr("hullHpBonus") * level)