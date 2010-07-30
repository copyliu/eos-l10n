#Item: Advanced Weapon Upgrades [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Bomb Deployment"),
                                  "power", skill.getModifiedItemAttr("powerNeedBonus") * skill.level)
