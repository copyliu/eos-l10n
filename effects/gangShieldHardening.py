#Item: Siege Warfare Link - Shield Harmonizing [Module]
type = "gang", "active"
def handler(fit, module, context):
    if "gang" not in context: return
    for damageType in ("Em", "Explosive", "Thermal", "Kinetic"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % damageType,
                               module.getModifiedItemAttr("commandBonus"),
                               stackingPenalties = True)
