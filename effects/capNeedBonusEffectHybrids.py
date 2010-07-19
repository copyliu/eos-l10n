#Variations of item: Large Hybrid Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Medium Hybrid Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Small Hybrid Discharge Elutriation I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Hybrid Weapon",
                                  "capacitorNeed", module.getModifiedItemAttr("capNeedBonus"))