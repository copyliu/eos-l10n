#Item: Mining Foreman Link - Laser Optimization [Module]
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Mining Laser", "Strip Miner", "Frequency Mining Laser",
              "Ice Harvester", "Gas Cloud Harvester")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "duration", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
