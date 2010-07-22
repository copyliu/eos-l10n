#Item: Grail Alpha [Implant]
#Item: Grail Beta [Implant]
#Item: Grail Delta [Implant]
#Item: Grail Epsilon [Implant]
#Item: Grail Gamma [Implant]
#Item: Grail Omega [Implant]
type = "passive"
runTim = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "scanRadarStrengthPercent" in implant.itemModifiedAttributes and\
                                      "implantSetImperialNavy" in implant.itemModifiedAttributes,
                                      "scanRadarStrengthPercent", implant.getModifiedItemAttr("implantSetImperialNavy"))