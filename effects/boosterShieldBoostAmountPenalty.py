#Items from group: Booster (6 of 34) [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Booster",
                                  "shieldBonus", booster.getModifiedItemAttr("boosterShieldBoostAmountPenalty"))