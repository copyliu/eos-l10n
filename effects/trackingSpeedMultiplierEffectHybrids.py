#Variations of item: Large Hybrid Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Medium Hybrid Metastasis Adjuster I (2 of 2) [Module]
#Variations of item: Small Hybrid Metastasis Adjuster I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Hybrid Weapon",
                                  "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"))