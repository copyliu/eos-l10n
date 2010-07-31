#Used by:
#Modules from group: Rig Astronautic (48 of 48)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("drawback"))