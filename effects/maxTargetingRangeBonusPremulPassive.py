#Variations of item: Large Ionic Field Projector I (2 of 2) [Module]
#Variations of item: Medium Ionic Field Projector I (2 of 2) [Module]
#Variations of item: Small Ionic Field Projector I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeMultiplier"),
                              stackingPenalties = True)