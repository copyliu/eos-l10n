#Items with name like: Cargohold Optimization (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("capacity", module.getModifiedItemAttr("cargoCapacityBonus"))