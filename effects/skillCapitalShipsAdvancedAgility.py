#Item: Capital Ships [Skill]
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Ships"),
                                  "agility", skill.getModifiedItemAttr("agilityBonus") * skill.level)