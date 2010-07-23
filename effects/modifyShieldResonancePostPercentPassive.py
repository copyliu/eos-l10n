#Items from group: Rig Shield (24 of 54) [Module]
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % type.capitalize(),
                               module.getModifiedItemAttr("%sDamageResistanceBonus" % type),
                               stackingPenalties = True)