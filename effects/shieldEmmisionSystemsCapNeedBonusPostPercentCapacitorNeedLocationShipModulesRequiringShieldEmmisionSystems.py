#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Shield Implants (3 of 3)
#Item: Shield Emission Systems [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Emission Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)