# Used by:
# Implants named like: Zainou 'Gnome' Shield Upgrades SU (6 of 6)
# Modules named like: Core Defense Charge Economizer (6 of 6)
# Skill: Shield Upgrades
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Upgrades"),
                                  "power", container.getModifiedItemAttr("powerNeedBonus") * level)
