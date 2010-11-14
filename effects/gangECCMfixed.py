#Used by:
#Module: Information Warfare Link - Sensor Integrity
type = "gang", "active"
gangBoost = "scanTypeStrength"
def handler(fit, module, context):
    if "gang" not in context: return
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        fit.ship.boostItemAttr("scan%sStrength" % scanType,
                               module.getModifiedItemAttr("commandBonus"),
                               stackingPenalties = True)
