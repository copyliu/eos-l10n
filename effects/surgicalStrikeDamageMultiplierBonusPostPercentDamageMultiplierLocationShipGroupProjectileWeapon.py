#Item: Surgical Strike [Skill]
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)