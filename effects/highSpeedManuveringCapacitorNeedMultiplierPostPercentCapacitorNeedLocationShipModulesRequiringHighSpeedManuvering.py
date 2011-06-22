# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Rogue' GY (6 of 6)
# Skill: High Speed Maneuvering
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                  "capacitorNeed", container.getModifiedItemAttr("capacitorNeedMultiplier") * level)
