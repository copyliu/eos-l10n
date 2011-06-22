# Used by:
# Celestials named like: Black Hole Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                     "maxRange", module.getModifiedItemAttr("maxRangeMultiplier"))