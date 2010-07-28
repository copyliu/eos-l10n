#Item: Improved Drop Booster [Implant]
#Item: Standard Drop Booster [Implant]
#Item: Strong Drop Booster [Implant]
#Item: Synth Drop Booster [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "trackingSpeed", implant.getModifiedItemAttr("trackingSpeedMultiplier"))