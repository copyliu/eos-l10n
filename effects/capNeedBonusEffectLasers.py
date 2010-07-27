#Variations of item: Large Energy Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Medium Energy Discharge Elutriation I (2 of 2) [Module]
#Variations of item: Small Energy Discharge Elutriation I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoostr(lambda mod: mod.item.group.name == "Energy Weapon",
                                   "capacitorNeed", module.getModifiedItemAttr("capNeedBonus"))