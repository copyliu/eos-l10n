#Item: Spur Alpha [Implant]
#Item: Spur Beta [Implant]
#Item: Spur Delta [Implant]
#Item: Spur Epsilon [Implant]
#Item: Spur Gamma [Implant]
#Item: Spur Omega [Implant]
type = "passive"
runTime = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetFederationNavy" in implant.itemModifiedAttributes and\
                                   "scanMagnetometricStrengthPercent" in implant.itemModifiedAttributes,
                                   "scanMagnetometricStrengthPercent", implant.getModifiedItemAttr("implantSetFederationNavy"))