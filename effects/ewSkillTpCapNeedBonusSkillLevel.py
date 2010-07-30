#Used by:
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Electronics Implants (6 of 12)
#Skill: Target Painting
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Target Painting"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
