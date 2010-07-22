#Item: Skirmish Warfare Link - Interdiction Maneuvers [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = ("Stasis Web","Warp Scrambler")
    fit.modules.filteredItemBoost(lambda mod: mod.group.name in groups,
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)