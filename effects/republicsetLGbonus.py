#Item: Low-grade Jackal Alpha [Implant]
#Item: Low-grade Jackal Beta [Implant]
#Item: Low-grade Jackal Delta [Implant]
#Item: Low-grade Jackal Epsilon [Implant]
#Item: Low-grade Jackal Gamma [Implant]
#Item: Low-grade Jackal Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetLGRepublicFleet" in implant.itemModifiedAttributes and\
                                   "scanLadarStrengthPercent" in implant.itemModifiedAttributes,
                                   "scanLadarStrengthPercent", implant.getModifiedItemAttr("implantSetLGRepublicFleet"))