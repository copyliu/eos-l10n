#Item: Fuel Conservation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Afterburner"),
                                  "capacitorNeed", skill.getModifiedItemAttr("capNeedBonus") * skill.level)