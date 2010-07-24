#Items from group: Cyberimplant (12 of 138) [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "velocityBonus" in implant.itemModifiedAttributes and \
                                      "implantSetSerpentis" in implant.itemModifiedAttributes,
                                      "velocityBonus", implant.getModifiedItemAttr("implantSetSerpentis"))