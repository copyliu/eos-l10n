#Used by:
#Items from category: Subsystem (40 of 80)
type = "passive"
runTime = "early"
def handler(fit, module, context):
    fit.ship.boostItemAttr("powerOutput", module.getModifiedItemAttr("powerOutput"))
