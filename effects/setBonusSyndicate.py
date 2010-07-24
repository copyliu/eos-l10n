#Item: Low-grade Edge Alpha [Implant]
#Item: Low-grade Edge Beta [Implant]
#Item: Low-grade Edge Delta [Implant]
#Item: Low-grade Edge Epsilon [Implant]
#Item: Low-grade Edge Gamma [Implant]
#Item: Low-grade Edge Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "boosterAttributeModifier" in implant.itemModifiedAttributes and \
                                      "implantSetSyndicate" in implant.itemModifiedAttributes,
                                      "boosterAttributeModifier", implant.getModifiedItemAttr("implantSetSyndicate"))