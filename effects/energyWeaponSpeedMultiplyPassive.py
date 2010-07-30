#Used by:
#Modules named like: Energy Burst Aerator (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)