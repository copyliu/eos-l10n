#Variations of item: Mining Laser Upgrade I (6 of 6) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "cpu", module.getModifiedItemAttr("cpuPenaltyPercent"))