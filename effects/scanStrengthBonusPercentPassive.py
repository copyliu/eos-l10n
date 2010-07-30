#Used by:
#Implants from group: Cyberimplant (20 of 138)
type = "passive"
def handler(fit, module, context):
    for type in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr("scan%sStrength" % type,
                               module.getModifiedItemAttr("scan%sStrengthPercent" % type),
                               stackingPenalties = True)