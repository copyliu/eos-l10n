#Used by:
#Module: Skirmish Warfare Link - Evasive Maneuvers
type = "gang", "active"
gangBoost = "signatureRadius"
def handler(fit, module, context):
    if "gang" not in context: return
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("commandBonus"),
                           stackingPenalties = True)
