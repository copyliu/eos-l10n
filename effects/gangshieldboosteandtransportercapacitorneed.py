# Used by:
# Variations of module: Siege Warfare Link - Shield Efficiency (2 of 2)
type = "gang", "active"
gangBoost = "shieldRepairCapacitorNeed"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Shield Booster","Shield Transporter")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
