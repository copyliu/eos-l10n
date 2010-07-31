#Used by:
#Celestials named like: Red Giant Beacon Class (6 of 6)
type= "projected"
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: "heatDamage" in mod.itemModifiedAttributes,
                                     "heatDamage", module.getModifiedItemAttr("heatDamageMultiplier"))