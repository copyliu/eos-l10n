# Used by:
# Module: Warp Disruption Field Generator I
type = "active"
runTime = "early"
def handler(fit, module, context):
    fit.ship.boostItemAttr("mass", module.getModifiedItemAttr("massBonusPercentage"))
    fit.ship.boostItemAttr("signatureRadius", module.getModifiedItemAttr("signatureRadiusBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedBoostFactor", module.getModifiedItemAttr("speedBoostFactorBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", module.getModifiedItemAttr("speedFactorBonus"))
    fit.ship.forceItemAttr("disallowAssistance", 1)
