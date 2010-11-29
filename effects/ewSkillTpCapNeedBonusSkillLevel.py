#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KSB (3 of 3)
#Implants named like: Hardwiring Zainou 'Gypsy' KTB (3 of 3)
#Skill: Target Painting
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Target Painting"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
