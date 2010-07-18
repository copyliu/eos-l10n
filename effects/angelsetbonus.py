#Items from group: Cyberimplant (12 of 138)
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.implants.filteredItemMultiply(
        lambda implant: "signatureRadiusBonus" in implant.attributes and "implantSetAngel" in implant.attributes,
        "signatureRadiusBonus",
        implant.getModifiedItemAttr("implantSetAngel"))