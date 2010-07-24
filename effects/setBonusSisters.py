#Item: Low-grade Virtue Alpha [Implant]
#Item: Low-grade Virtue Beta [Implant]
#Item: Low-grade Virtue Delta [Implant]
#Item: Low-grade Virtue Epsilon [Implant]
#Item: Low-grade Virtue Gamma [Implant]
#Item: Low-grade Virtue Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "scanStrengthBonus" in implant.itemModifiedAttributes and \
                                      "implantSetSisters" in implant.itemModifiedAttributes,
                                      "scanStrengthBonus", implant.getModifiedItemAttr("implantSetSisters"))