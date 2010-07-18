#Item: Improved Mindflood Booster [Implant]
#Item: Standard Mindflood Booster [Implant]
#Item: Strong Mindflood Booster [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Booster",
                                  "shieldBonus", booster.getModifiedItemAttr("shieldBoostMultiplier"))