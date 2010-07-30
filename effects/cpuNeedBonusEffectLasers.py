#Items with name like: Algid Energy Administrations Unit (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "cpu", module.getModifiedItemAttr("cpuNeedBonus"))