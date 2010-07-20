#Items from group: Rig Astronautic (48 of 48) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("drawback"))