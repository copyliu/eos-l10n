#Variations of item: Large Energy Locus Coordinator I (2 of 2) [Module]
#Variations of item: Medium Energy Locus Coordinator I (2 of 2) [Module]
#Variations of item: Small Energy Locus Coordinator I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "maxRange", module.getModifiedItemAttr("maxRangeBonus"),
                                  stackingPenalties = True)