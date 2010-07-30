#Items with name like: Liquid Cooled Electronics (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Electronics Implants (3 of 6)
#Item: Electronics Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Electronics Upgrades"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus") * level)
