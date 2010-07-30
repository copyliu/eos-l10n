#Items with name like: Magnetar Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                     "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"))