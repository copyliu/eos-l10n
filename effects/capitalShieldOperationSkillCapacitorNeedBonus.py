# Used by:
# Skill: Capital Shield Operation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Operation"),
                                  "capacitorNeed", skill.getModifiedItemAttr("shieldBoostCapacitorBonus") * skill.level)