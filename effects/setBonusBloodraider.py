#Items from group: Cyberimplant (12 of 138) [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "durationBonus" in implant.itemModifiedAttributes and \
                                   "implantSetBloodraider" in implant.itemModifiedAttributes,
                                   "durationBonus", implant.getModifiedItemAttr("implantSetBloodraider"))