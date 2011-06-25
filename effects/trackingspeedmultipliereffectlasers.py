# Used by:
# Modules named like: Energy Metastasis Adjuster (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"),
                                     stackingPenalties = True)
