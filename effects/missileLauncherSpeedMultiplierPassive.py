#Used by:
#Modules named like: Bay Loading Accelerator (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties = True)
