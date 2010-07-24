#Items from group: Cyberimplant (13 of 138) [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "armorHpBonus" in implant.itemModifiedAttributes and \
                                      "implantSetSansha" in implant.itemModifiedAttributes,
                                      "armorHpBonus", implant.getModifiedItemAttr("implantSetSansha"))