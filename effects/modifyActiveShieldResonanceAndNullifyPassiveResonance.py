#Items from group: Shield Hardener (91 of 91) [Module]
type = "active"
def handler(fit, module, context):
    for damageType in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % damageType.capitalize(),
                               module.getModifiedItemAttr("%sDamageResistanceBonus") % damageType,
                               stackingPenalties = True)