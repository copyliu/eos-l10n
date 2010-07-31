#Used by:
#Implants named like: Low grade Talon (6 of 6)
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemBoost(lambda implant: "implantSetLGCaldariNavy" in implant.itemModifiedAttributes and\
                                   "scanGravimetricStrengthModifier" in implant.itemModifiedAttributes,
                                   "scanGravimetricStrengthModifier", implant.getModifiedItemAttr("implantSetLGCaldariNavy"))