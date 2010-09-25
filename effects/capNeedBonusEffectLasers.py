#Used by:
#Modules named like: Energy Discharge Elutriation (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "capacitorNeed", module.getModifiedItemAttr("capNeedBonus"))
