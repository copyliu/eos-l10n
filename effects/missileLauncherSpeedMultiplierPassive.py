#Items with name like: Bay Loading Accelerator (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name[0:16] == "Missile Launcher",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)