# Used by:
# Implants named like: Hardwiring Zainou 'Gypsy' KTB (6 of 6)
# Skill: Target Painting
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Target Painting"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
