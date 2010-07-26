#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadSpeedFactorBonus" in mod.itemModifiedAttributes,
                                     "overloadSpeedFactorBonus", module.getModifiedItemAttr("overloadBonusMultiplier"))