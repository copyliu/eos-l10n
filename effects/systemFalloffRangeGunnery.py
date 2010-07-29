#Items with name like: Black Hole Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                     "falloff", module.getModifiedItemAttr("fallofMultiplier"))