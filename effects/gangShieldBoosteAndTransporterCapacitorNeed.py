#Item: Siege Warfare Link - Shield Efficiency [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = ("Shield Booster","Shield Transporter")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)