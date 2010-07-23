#Item: Jackal Alpha [Implant]
#Item: Jackal Beta [Implant]
#Item: Jackal Delta [Implant]
#Item: Jackal Epsilon [Implant]
#Item: Jackal Gamma [Implant]
#Item: Jackal Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetRepublicFleet" in implant.itemModifiedAttributes and\
                                   "scanLadarStrengthPercent" in implant.itemModifiedAttributes,
                                   "scanLadarStrengthPercent", implant.getModifiedItemAttr("implantSetRepublicFleet"))