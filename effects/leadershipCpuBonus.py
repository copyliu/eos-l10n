#Items from group: Battlecruiser (8 of 8) [Ship]
#Items from group: Command Ship (8 of 8) [Ship]
#Items from group: Titan (4 of 4) [Ship]
#Items with name like: Defensive - Warfare Processor (4 of 4)
#Items from market group: Ships > Capital Industrial Ships (2 of 2)
#Items from market group: Ships > Carriers (8 of 8)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus"))