#Variations of item: Large Hybrid Locus Coordinator I (2 of 2) [Module]
#Variations of item: Medium Hybrid Locus Coordinator I (2 of 2) [Module]
#Variations of item: Small Hybrid Locus Coordinator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Hybrid Weapon",
                                  "maxRange", module.getModifiedItemAttr("maxRangeBonus"),
                                  stackingPenalties = True)