#Item: Low-grade Harvest Alpha [Implant]
#Item: Low-grade Harvest Beta [Implant]
#Item: Low-grade Harvest Delta [Implant]
#Item: Low-grade Harvest Epsilon [Implant]
#Item: Low-grade Harvest Gamma [Implant]
#Item: Low-grade Harvest Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "maxRangeBonus" in implant.itemModifiedAttributes and \
                                      "implantSetORE" in implant.itemModifiedAttributes,
                                      "maxRangeBonus", implant.getModifiedItemAttr("implantSetORE"))