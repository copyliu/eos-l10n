#Used by:
#Modules from group: Rig Electronics Superiority (48 of 48)
type = "passive"
def handler(fit, modules, context):
    fit.ship.boostItemAttr("shieldCapacity", module.getModifiedItemAttr("drawback"))