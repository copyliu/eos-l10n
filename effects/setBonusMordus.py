#Item: Low-grade Centurion Alpha [Implant]
#Item: Low-grade Centurion Beta [Implant]
#Item: Low-grade Centurion Delta [Implant]
#Item: Low-grade Centurion Epsilon [Implant]
#Item: Low-grade Centurion Gamma [Implant]
#Item: Low-grade Centurion Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "rangeSkillBonus" in implant.itemModifiedAttributes and \
                                   "implantSetMordus" in implant.itemModifiedAttributes,
                                   "rangeSkillBonus", implant.getModifiedItemAttr("implantSetMordus"))