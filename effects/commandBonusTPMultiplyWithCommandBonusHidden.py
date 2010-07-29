#Item: Information Warfare Link - Electronic Superiority [Module]
type = "active", "gang"
def handler(fit, module, context):
    if "gang" not in context: return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Target Painter",
                                  "signatureRadiusBonus", module.getModifiedItemAttr("commandBonusTP") * mult,
                                  stackingPenalties = True)
