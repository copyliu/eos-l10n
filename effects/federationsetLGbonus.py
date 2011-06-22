# Used by:
# Implants named like: Low grade Spur (6 of 6)
type = "passive"
runTime = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetLGFederationNavy" in implant.itemModifiedAttributes \
                                      and "scanMagnetometricStrengthModifier" in implant.itemModifiedAttributes,
                                      "scanMagnetometricStrengthModifier", implant.getModifiedItemAttr("implantSetLGFederationNavy"))