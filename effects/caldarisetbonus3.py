#Item: Talon Alpha [Implant]
#Item: Talon Beta [Implant]
#Item: Talon Delta [Implant]
#Item: Talon Epsilon [Implant]
#Item: Talon Gamma [Implant]
#Item: Talon Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetCaldariNavy" in implant.itemModifiedAttributes and\
                                      "scanGravimetricStrengthPercent" in implant.itemModifiedAttributes,
                                      "scanGravimetricStrengthPercent", implant.getModifiedAttribute("implantSetCaldariNavy"))