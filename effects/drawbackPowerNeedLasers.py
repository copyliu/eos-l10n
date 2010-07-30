#Used by:
#Modules from group: Rig Energy Weapon (42 of 42)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "power", module.getModifiedItemAttr("drawback"))