#Used by:
#Modules named like: Anti Screen Reinforcer (24 of 24)
type = "passive"
def handler(fit, module, context):
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % type.capitalize(),
                               module.getModifiedItemAttr("%sDamageResistanceBonus" % type),
                               stackingPenalties = True)