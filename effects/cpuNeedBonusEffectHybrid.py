#Used by:
#Modules named like: Algid Hybrid Administrations Unit (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "cpu", module.getModifiedItemAttr("cpuNeedBonus"))