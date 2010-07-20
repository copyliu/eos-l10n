#Items from group: Rig Hybrid Weapon (42 of 42) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Hybrid Weapon",
                                  "power", module.getModifiedItemAttr("drawback"))