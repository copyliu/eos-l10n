#Used by:
#Implants named like: Hardwiring Zainou 'Gnome' KUA (3 of 3)
#Modules named like: Core Defence Charge Economizer (6 of 6)
#Skill: Shield Upgrades
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Upgrades"),
                                  "power", container.getModifiedItemAttr("powerNeedBonus") * level)
