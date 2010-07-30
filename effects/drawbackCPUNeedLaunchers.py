#Items from group: Rig Launcher (36 of 36) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name[0:16] == "Missile Launcher",
                                  "cpu", module.getModifiedItemAttr("drawback"))