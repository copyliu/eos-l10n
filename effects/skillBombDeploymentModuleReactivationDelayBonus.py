#Item: Bomb Deployment [Skill]
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Bomb",
                                  "moduleReactivationDelay", skill.getModifiedItemAttr("rofBonus") * skill.level)