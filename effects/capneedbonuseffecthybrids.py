# Used by:
# Modules named like: Hybrid Discharge Elutriation (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "capacitorNeed", module.getModifiedItemAttr("capNeedBonus"))