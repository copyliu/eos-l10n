#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Shield Implants (3 of 3)
#Variations of item: Large Core Defence Charge Economizer I (2 of 2) [Module]
#Variations of item: Medium Core Defence Charge Economizer I (2 of 2) [Module]
#Variations of item: Small Core Defence Charge Economizer I (2 of 2) [Module]
#Item: Shield Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Upgrades"),
                                  "power", container.getModifiedItemAttr("powerNeedBonus") * level)
