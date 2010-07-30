#Used by:
#Module: Skirmish Warfare Link - Interdiction Maneuvers
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Stasis Web","Warp Scrambler")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
