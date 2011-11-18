# Used by:
# Skill: Neurobiology
type = "passive"
def handler(fit, skill, context):
    fit.boosters.filteredItemBoost(lambda booster: True, "shieldBoostMultiplier",
                                   skill.getModifiedItemAttr("skillBonusBooster") * skill.level)
