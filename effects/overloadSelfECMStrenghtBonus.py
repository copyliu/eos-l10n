#Items from group: ECM (44 of 44) [Module]
type = "overheat"
def handler(fit, module, context):
    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        module.boostItemAttr("scan%StrengthBonus" % scanType,
                             module.getModifiedItemAttr("overloadECMStrengthBonus"),
                             stackingPenalties = True)