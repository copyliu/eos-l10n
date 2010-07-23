#Items from category: Subsystem (40 of 80)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("powerOutput"))