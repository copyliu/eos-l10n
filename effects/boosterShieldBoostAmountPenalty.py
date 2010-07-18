#Items from market group: Implants & Boosters > Booster (6 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Booster",
                                  "shieldBonus", booster.getModifiedItemAttr("boosterShieldBoostAmountPenalty"))