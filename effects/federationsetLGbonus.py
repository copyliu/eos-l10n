#Item: Low-grade Spur Alpha [Implant]
#Item: Low-grade Spur Beta [Implant]
#Item: Low-grade Spur Delta [Implant]
#Item: Low-grade Spur Epsilon [Implant]
#Item: Low-grade Spur Gamma [Implant]
#Item: Low-grade Spur Omega [Implant]
type = "passive"
runTime = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetLGFederationNavy" in implant.itemModifiedAttributes \
                                      and "scanMagnetometricStrengthModifier" in implant.itemModifiedAttributes,
                                      "scanMagnetometricStrengthModifier", implant.getModifiedItemAttr("implantSetLGFederationNavy"))