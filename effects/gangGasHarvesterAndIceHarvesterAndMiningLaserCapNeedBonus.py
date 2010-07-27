#Item: Mining Foreman Link - Harvester Capacitor Efficiency [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = ("Mining Laser", "Strip Miner", "Frequency Mining Laser",
              "Ice Harvester", "Gas Cloud Harvester")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)