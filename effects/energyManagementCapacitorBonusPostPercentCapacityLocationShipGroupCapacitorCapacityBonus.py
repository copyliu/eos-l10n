#Items with name like: Mindflood Booster (4 of 4)
#Items with name like: Semiconductor Memory Cell (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Engineering Implants (3 of 3)
#Item: Energy Management [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("capacitorCapacityBonus") * level)
