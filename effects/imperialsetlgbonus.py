# Used by:
# Implants named like: Low grade Grail (6 of 6)
type = "passive"
runTime = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "scanRadarStrengthModifier" in implant.itemModifiedAttributes,
                                      "scanRadarStrengthModifier", implant.getModifiedItemAttr("implantSetLGImperialNavy"))
