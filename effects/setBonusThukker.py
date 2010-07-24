#Item: Low-grade Nomad Alpha [Implant]
#Item: Low-grade Nomad Beta [Implant]
#Item: Low-grade Nomad Delta [Implant]
#Item: Low-grade Nomad Epsilon [Implant]
#Item: Low-grade Nomad Gamma [Implant]
#Item: Low-grade Nomad Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "agilityBonus" in implant.itemModifiedAttributes and \
                                      "implantSetThukker" in implant.itemModifiedAttributes,
                                      "agilityBonus", implant.getModifiedItemAttr("implantSetThukker"))