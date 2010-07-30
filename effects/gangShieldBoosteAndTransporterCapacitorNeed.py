#Used by:
#Module: Siege Warfare Link - Shield Efficiency
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Shield Booster","Shield Transporter")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
