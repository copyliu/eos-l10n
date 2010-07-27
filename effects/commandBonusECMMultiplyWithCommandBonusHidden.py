#Item: Information Warfare Link - Electronic Superiority [Module]
type = "active", "gang"
def handler(fit, module, context):
    if context != "gang": return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for scanType in ("Magnetometric", "Radar", "Ladar", "Gravimetric"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                      "scan%sStrengthBonus" % scanType,
                                      module.getModifiedItemAttr("commandBonusECM") * mult,
                                      stackingPenalties = True)