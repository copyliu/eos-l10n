#Items from group: ECM Stabilizer (6 of 6) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "scanRadarStrengthBonus", module.getModifiedItemAttr("scanStrengthBonus"),
                                  stackingPenalties = True)