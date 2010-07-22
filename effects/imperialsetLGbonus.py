#Item: Low-grade Grail Alpha [Implant]
#Item: Low-grade Grail Beta [Implant]
#Item: Low-grade Grail Delta [Implant]
#Item: Low-grade Grail Epsilon [Implant]
#Item: Low-grade Grail Gamma [Implant]
#Item: Low-grade Grail Omega [Implant]
type = "passive"
runTim = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "scanRadarStrengthPercent" in implant.itemModifiedAttributes and\
                                      "implantSetLGImperialNavy" in implant.itemModifiedAttributes,
                                      "scanRadarStrengthPercent", implant.getModifiedItemAttr("implantSetLGImperialNavy"))