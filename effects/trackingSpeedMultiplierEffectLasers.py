#Variations of item: Large Energy Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Medium Energy Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Small Energy Metastasis Adjuster I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Energy Weapon",
                                  "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"))