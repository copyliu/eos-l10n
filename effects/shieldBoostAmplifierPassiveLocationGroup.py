#Items from group: Booster (5 of 34) [Implant]
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Booster",
                                  "shieldBonus", container.getModifiedItemAttr("shieldBoostMultiplier"))