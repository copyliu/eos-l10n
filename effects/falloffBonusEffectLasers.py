#Variations of item: Large Energy Ambit Extension I (2 of 2) [Module]
#Variations of item: Medium Energy Ambit Extension I (2 of 2) [Module]
#Variations of item: Small Energy Ambit Extension I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Energy Weapon",
                                  "falloff", module.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties = True)