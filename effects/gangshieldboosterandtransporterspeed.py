# Used by:
# Module: Siege Warfare Link - Active Shielding
type = "gang", "active"
gangBoost = "shieldRepairDuration"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Shield Booster","Shield Transporter")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "duration", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
