#Variations of item: Large Energy Burst Aerator I (2 of 2) [Module]
#Variations of item: Medium Energy Burst Aerator I (2 of 2) [Module]
#Variations of item: Small Energy Burst Aerator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Energy Weapon",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)