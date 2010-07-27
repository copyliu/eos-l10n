#Variations of item: Large Algid Hybrid Administrations Unit I (2 of 2) [Module]
#Variations of item: Medium Algid Hybrid Administrations Unit I (2 of 2) [Module]
#Variations of item: Small Algid Hybrid Administrations Unit I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "cpu", module.getModifiedItemAttr("cpuNeedBonus"))