# Used by:
# Implants named like: Drop Booster (4 of 4)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", implant.getModifiedItemAttr("trackingSpeedMultiplier"))