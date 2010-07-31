#Used by:
#Implants named like: Mindflood Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", booster.getModifiedItemAttr("shieldBoostMultiplier"))