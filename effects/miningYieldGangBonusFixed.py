#Item: Mining Foreman [Skill]
#Item: Mining Foreman Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                   "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)