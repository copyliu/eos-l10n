#Items from group: Rig Energy Grid (6 of 30) [Module]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Engineering Implants (3 of 3)
#Item: Energy Management [Skill]
#Item: Improved Mindflood Booster [Implant]
#Item: Standard Mindflood Booster [Implant]
#Item: Strong Mindflood Booster [Implant]
#Item: Synth Mindflood Booster [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("capacitorCapacity", container.getModifiedItemAttr("capacitorCapacityBonus") * level)
