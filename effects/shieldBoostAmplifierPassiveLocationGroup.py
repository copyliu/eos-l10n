#Used by:
#Implants named like: Blue Pill Booster (5 of 5)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "shieldBonus", container.getModifiedItemAttr("shieldBoostMultiplier"))