# Used by:
# Modules named like: Targeting Systems Stabilizer (6 of 6)
type = "offline"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda module: module.item.requiresSkill("Cloaking"),
                                  "cloakingTargetingDelay", module.getModifiedItemAttr("cloakingTargetingDelayBonus"))
