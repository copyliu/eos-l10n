#Items from group: ECM Stabilizer (6 of 6) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanLadarStrengthBonus", module.getModifiedItemAttr("scanStrengthBonus"),
                                  stackingPenalties = True)