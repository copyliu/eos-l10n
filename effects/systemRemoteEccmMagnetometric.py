#Items with name like: Magnetar Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projected ECCM",
                                     "scanMagnetometricStrengthBonus", module.getModifiedItemAttr("scanMagnetometricStrengthMultiplier"))