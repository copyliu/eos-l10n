#Used by:
#Modules from group: Ballistic Control system (21 of 21)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name[0:16] == "Missile Launcher",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)
