#Used by:
#Module: Warp Disruption Field Generator I
type = "active"
def handler(fit, module, context):
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadiusBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", module.getModifiedItemAttr("speedFactorBonus"))
    fit.ship.itemModifiedAttributes["disallowAssistance"] =  1