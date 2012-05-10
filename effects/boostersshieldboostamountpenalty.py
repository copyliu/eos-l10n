# Used by:
# Implants named like: Mindflood Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation") or mod.item.requiresSkill("Capital Shield Operation"),
                                  "shieldBonus", booster.getModifiedItemAttr("shieldBoostMultiplier"))
