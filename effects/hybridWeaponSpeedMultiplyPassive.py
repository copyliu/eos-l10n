#Variations of item: Large Hybrid Burst Aerator I (2 of 2) [Module]
#Variations of item: Medium Hybrid Burst Aerator I (2 of 2) [Module]
#Variations of item: Small Hybrid Burst Aerator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Hybrid Weapon",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)