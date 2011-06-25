# Used by:
# Modules named like: Hybrid Metastasis Adjuster (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                     "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier")
                                     stackingPenalties = True)
