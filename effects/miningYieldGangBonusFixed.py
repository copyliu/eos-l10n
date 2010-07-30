#Item: Mining Foreman [Skill]
#Item: Mining Foreman Mindlink [Implant]
type = "gang"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                   "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)
