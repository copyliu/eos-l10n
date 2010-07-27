#Variations of item: Large Hybrid Ambit Extension I (2 of 2) [Module]
#Variations of item: Medium Hybrid Ambit Extension I (2 of 2) [Module]
#Variations of item: Small Hybrid Ambit Extension I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "falloff", module.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties = True)