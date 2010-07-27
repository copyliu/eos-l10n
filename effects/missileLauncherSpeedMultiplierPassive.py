#Variations of item: Large Bay Loading Accelerator I (2 of 2) [Module]
#Variations of item: Medium Bay Loading Accelerator I (2 of 2) [Module]
#Variations of item: Small Bay Loading Accelerator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name[0:16] == "Missile Launcher",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)