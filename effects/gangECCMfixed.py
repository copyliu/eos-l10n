#Item: Information Warfare Link - Sensor Integrity [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    for scanType in ("Gravimetric", "Radar", "Ladar", "Magnetometric"):
        fit.ship.boostItemAttr("scan%sStrength" % scanType,
                               module.getModifiedItemAttr("commandBonus"),
                               stackingPenalties = True)