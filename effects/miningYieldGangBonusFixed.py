#Used by:
#Implant: Mining Foreman Mindlink
#Skill: Mining Foreman
type = "gang", "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    if "gang" in context:
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                      "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)
    else:
        container.commandBonus = container.getModifiedItemAttr("miningAmountBonus") * level
