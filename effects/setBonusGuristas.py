#Items with name like: Crystal (12 of 45)
#Items with name like: Low-grade Crystal (6 of 6)
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "shieldBoostMultiplier" in implant.itemModifiedAttributes and \
                                   "implantSetGuristas" in implant.itemModifiedAttributes,
                                   "shieldBoostMultiplier", implant.getModifiedItemAttr("implantSetGuristas"))