#Item: Low-grade Harvest Alpha [Implant]
#Item: Low-grade Harvest Beta [Implant]
#Item: Low-grade Harvest Delta [Implant]
#Item: Low-grade Harvest Epsilon [Implant]
#Item: Low-grade Harvest Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Mining Laser",
                                  "maxRange", implant.getModifiedItemAttr("maxRangeBonus"))