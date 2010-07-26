#Variations of item: Large Cargohold Optimization I (2 of 2) [Module]
#Variations of item: Medium Cargohold Optimization I (2 of 2) [Module]
#Variations of item: Small Cargohold Optimization I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("capacity", module.getModifiedItemAttr("cargoCapacityBonus"))