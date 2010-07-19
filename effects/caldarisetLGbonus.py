#Item: Low-grade Talon Alpha [Implant]
#Item: Low-grade Talon Beta [Implant]
#Item: Low-grade Talon Delta [Implant]
#Item: Low-grade Talon Epsilon [Implant]
#Item: Low-grade Talon Gamma [Implant]
#Item: Low-grade Talon Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemBoost(lambda implant: "implantSetLGCaldariNavy" in implant.itemModifiedAttributes and\
                                   "scanGravimetricStrengthModifier" in implant.itemModifiedAttributes,
                                   "scanGravimetricStrengthModifier", implant.getModifiedItemAttr("implantSetLGCaldariNavy"))