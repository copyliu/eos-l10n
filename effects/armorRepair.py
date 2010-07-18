#Items from group: Armor Repair Unit (99 of 99) [Module]
runTime = "late"
type = "active"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("armorDamageAmount")
    speed = module.getModifiedItemAttr("duration") / 1000.0
    fit.ship.armorRepair += amount / speed