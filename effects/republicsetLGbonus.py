#Items with name like: Low-grade Jackal (6 of 6)
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "implantSetLGRepublicFleet" in implant.itemModifiedAttributes and\
                                   "scanLadarStrengthPercent" in implant.itemModifiedAttributes,
                                   "scanLadarStrengthPercent", implant.getModifiedItemAttr("implantSetLGRepublicFleet"))