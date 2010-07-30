#Item: Skirmish Warfare Link - Evasive Maneuvers [Module]
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("commandBonus"),
                           stackingPenalties = True)
