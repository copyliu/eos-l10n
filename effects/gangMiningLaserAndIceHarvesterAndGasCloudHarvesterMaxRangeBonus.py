#Item: Mining Foreman Link - Mining Laser Field Enhancement [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    groups = ("Mining Laser", "Strip Miner", "Frequency Mining Laser",
              "Ice Harvester", "Gas Cloud Harvester")
    fit.modules.filteredItemBoost(lambda mod: mod.group.name in groups,
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)