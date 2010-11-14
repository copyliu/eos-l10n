#Used by:
#Module: Mining Foreman Link - Mining Laser Field Enhancement
type = "gang", "active"
gangBoost = "miningMaxRange"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Mining Laser", "Strip Miner", "Frequency Mining Laser",
              "Ice Harvester", "Gas Cloud Harvester")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
