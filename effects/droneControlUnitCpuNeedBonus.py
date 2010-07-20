#Items from market group: Ships > Carriers (8 of 8)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Drone Control Unit",
                                  "cpu", ship.getModifiedItemAttr("cpuNeedBonus"))