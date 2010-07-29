#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Navigation Implants (3 of 3)
#Item: High Speed Maneuvering [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                  "capacitorNeed", container.getModifiedItemAttr("capacitorNeedMultiplier") * level)
