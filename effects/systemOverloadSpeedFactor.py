#Items with name like: Red Giant Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadSpeedFactorBonus" in mod.itemModifiedAttributes,
                                     "overloadSpeedFactorBonus", module.getModifiedItemAttr("overloadBonusMultiplier"))