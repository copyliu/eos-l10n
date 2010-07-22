#Item: Armored Warfare Link - Passive Defense [Module]
type = "gang", "active"
def handler(fit, module, context):
    if context != "gang": return
    for damageType in ("Em", "Thermal", "Explosive", "Kinetic"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % damageType,
                               module.getModifiedItemAttr("commandBonus"),
                               stackingPenalties = True)