#Items from group: Cyberimplant (20 of 138) [Implant]
type = "passive"
def handler(fit, module, context):
    for type in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr("scan%sStrength" % type,
                               module.getModifiedItemAttr("scan%sStrengthPercent" % type),
                               stackingPenalties = True)