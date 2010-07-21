#Item: Weapon Disruption [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Weapon Disruption"),
                                  "capacitorNeed", skill.getModifiedItemAttr("capNeedBonus") * skill.level)