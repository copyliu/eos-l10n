#Items with name like: Low-grade Grail (6 of 6)
type = "passive"
runTim = "early"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(lambda implant: "scanRadarStrengthPercent" in implant.itemModifiedAttributes and\
                                      "implantSetLGImperialNavy" in implant.itemModifiedAttributes,
                                      "scanRadarStrengthPercent", implant.getModifiedItemAttr("implantSetLGImperialNavy"))