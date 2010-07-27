#Variations of item: Large Algid Energy Administrations Unit I (2 of 2) [Module]
#Variations of item: Medium Algid Energy Administrations Unit I (2 of 2) [Module]
#Variations of item: Small Algid Energy Administrations Unit I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "cpu", module.getModifiedItemAttr("cpuNeedBonus"))