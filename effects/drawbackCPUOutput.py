#Used by:
#Modules from group: Rig Drones (48 of 48)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("cpuOutput", module.getModifiedItemAttr("drawback"))