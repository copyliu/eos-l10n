# Used by:
# Modules from group: Rig Hybrid Weapon (42 of 42)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "power", module.getModifiedItemAttr("drawback"))