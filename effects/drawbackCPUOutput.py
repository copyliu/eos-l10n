#Items from group: Rig Drones (48 of 48) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("drawback"))