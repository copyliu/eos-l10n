#Used by:
#Module: Information Warfare Link - Electronic Superiority
type = "active", "gang"
def handler(fit, module, context):
    if "gang" not in context: return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for scanType in ("Magnetometric", "Radar", "Ladar", "Gravimetric"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                      "scan%sStrengthBonus" % scanType,
                                      module.getModifiedItemAttr("commandBonusECM") * mult,
                                      stackingPenalties = True)
