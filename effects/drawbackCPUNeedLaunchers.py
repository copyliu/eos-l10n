#Used by:
#Modules from group: Rig Launcher (36 of 36)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name[0:16] == "Missile Launcher",
                                  "cpu", module.getModifiedItemAttr("drawback"))