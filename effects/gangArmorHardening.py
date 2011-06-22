# Used by:
# Module: Armored Warfare Link - Passive Defense
type = "gang", "active"
gangBoost = "armorResistance"
def handler(fit, module, context):
    if "gang" not in context: return
    for damageType in ("Em", "Thermal", "Explosive", "Kinetic"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % damageType,
                               module.getModifiedItemAttr("commandBonus"),
                               stackingPenalties = True)
