#Items with name like: Slave (12 of 12)
#Item: Halo Omega [Implant]
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "armorHpBonus" in implant.itemModifiedAttributes and \
                                      "implantSetSansha" in implant.itemModifiedAttributes,
                                      "armorHpBonus", implant.getModifiedItemAttr("implantSetSansha"))