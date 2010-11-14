#Used by:
#Implant: Mining Foreman Mindlink
#Skill: Mining Foreman
type = "gang"
gangBoost = "miningAmountBonus"
gangBonus = "miningAmount"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)
