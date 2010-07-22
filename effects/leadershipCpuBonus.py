#Items from group: Battlecruiser (8 of 8) [Ship]
#Items from group: Command Ship (8 of 8) [Ship]
#Items from group: Defensive Systems (4 of 16) [Subsystem]
#Items from group: Titan (4 of 4) [Ship]
#Items from market group: Ships > Capital Industrial Ships (2 of 2)
#Items from market group: Ships > Carriers (8 of 8)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus"))