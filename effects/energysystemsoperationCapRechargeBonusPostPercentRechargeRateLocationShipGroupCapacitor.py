#Items from group: Rig Energy Grid (6 of 30) [Module]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Engineering Implants (3 of 6)
#Item: Energy Systems Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.ship.boostItemAttr("rechargeRate", container.getModifiedItemAttr("capRechargeBonus") * level)
