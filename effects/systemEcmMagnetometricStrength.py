#Used by:
#Celestials named like: Magnetar Effect Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "ECM",
                                     "scanMagnetometricStrengthBonus", module.getModifiedItemAttr("scanMagnetometricStrengthMultiplier"))