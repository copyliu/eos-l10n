#Used by:
#Ships from group: Carrier (4 of 4)
#Ships from group: Supercarrier (4 of 4)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Drone Control Unit",
                                  "cpu", ship.getModifiedItemAttr("cpuNeedBonus"))