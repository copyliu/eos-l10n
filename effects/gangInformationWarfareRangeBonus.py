#Used by:
#Module: Information Warfare Link - Recon Operation
type = "gang", "active"
gangBoost = "electronicMaxRange"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Target Painter", "Tracking Disruptor", "Remote Sensor Damper", "ECM")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "maxRange", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
