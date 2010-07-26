#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadECCMStrenghtBonus" in mod.itemModifiedAttributes,
                                     "overloadECCMStrenghtBonus", module.getModifiedItemAttr("overloadBonusMultiplier"))