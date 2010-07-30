#Items with name like: Crash Booster (3 of 4)
#Items with name like: Frentix Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", booster.getModifiedItemAttr("boosterShieldBoostAmountPenalty"))