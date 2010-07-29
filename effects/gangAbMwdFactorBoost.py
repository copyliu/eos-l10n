#Item: Skirmish Warfare Link - Rapid Deployment [Module]
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
