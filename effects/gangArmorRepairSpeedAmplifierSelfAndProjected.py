#Item: Armored Warfare Link - Rapid Repair [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = "Armor Repair Unit", "Armor Repair Projector"
    fit.modules.filteredItemBoost(lambda mod: mod.group.name in groups,
                                  "duration", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)