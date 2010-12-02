#Used by:
#Implants named like: Crystal (12 of 12)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", container.getModifiedItemAttr("shieldBoostMultiplier"))
