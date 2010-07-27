#Item: Siege Warfare Link - Active Shielding [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = ("Shield Booster","Shield Transporter")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "duration", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)